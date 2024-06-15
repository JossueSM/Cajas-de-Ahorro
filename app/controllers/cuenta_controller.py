from flask import jsonify, request
from app import app
from app.services.cuenta_service import CuentaService

@app.route("/cuenta", methods=['GET'])
def cuenta():
    data = request.get_json()
    numero_cuenta = data.get("numero_cuenta")
    rows = CuentaService.obtener_cuenta(numero_cuenta)
    cuenta = [cuenta.as_dict() for cuenta in rows]
    return jsonify(cuenta)

@app.route("/cuentas", methods=['GET'])
def cuentas():
    rows = CuentaService.obtener_cuentas()
    cuentas = [cuentas.as_dict() for cuentas in rows]
    return jsonify(cuentas)

@app.route("/cuenta", methods=['POST'])
def cuenta_r():
    data = request.get_json()
    numero_cuenta=data.get("numero_cuenta")
    tipo_cuenta=data.get("tipo_cuenta")
    saldo_cuenta=data.get("saldo_cuenta")
    id_usuario=data.get("id_usuario")

    # Assuming UsuarioService.crear_usuario() returns an object with attributes
    nueva_cuenta = CuentaService.crear_cuenta(numero_cuenta,tipo_cuenta,saldo_cuenta,id_usuario)

    if nueva_cuenta:
        return jsonify({
            "mensaje": "Cuenta ingresada exitosamente",
            "Cuenta": {
                "numero_cuenta": nueva_cuenta.numero_cuenta,
                "tipo_cuenta": nueva_cuenta.tipo_cuenta,
                "saldo_cuenta": nueva_cuenta.saldo_cuenta,
                "id_usuario": nueva_cuenta.id_usuario
            }
        })
    else:
        return jsonify({
            "mensaje": "No se pudo crear la Cuenta"
        }), 400  
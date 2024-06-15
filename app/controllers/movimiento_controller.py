from flask import jsonify, request
from app import app
from app.services.movimiento_service import MovimientoService

@app.route("/movimiento", methods=['GET'])
def movimiento():
    data = request.get_json()
    numero_cuenta = data.get("numero_cuenta")
    rows = MovimientoService.obtener_movimiento(numero_cuenta)
    movimiento = [movimiento.as_dict() for movimiento in rows]
    return jsonify(movimiento)

@app.route("/movimientos", methods=['GET'])
def movimientos():
    rows = MovimientoService.obtener_usuarios()
    movimientos = [movimientos.as_dict() for movimientos in rows]
    return jsonify(movimientos)

@app.route("/movimiento", methods=['POST'])
def movimiento_r():
    data = request.get_json()
    tipo_movimiento = data.get("tipo_movimiento")
    numero_cuenta = data.get("numero_cuenta")

    nuevo_movimiento = MovimientoService.crear_movimiento(tipo_movimiento,numero_cuenta)

    if nuevo_movimiento:
        return jsonify({
            "mensaje": "Movimiento ingresado exitosamente",
            "Movimiento": {
                "tipo_movimiento": nuevo_movimiento.tipo_movimiento,
                "numero_cuenta": nuevo_movimiento.numero_cuenta,
            }
        })
    else:
        return jsonify({
            "mensaje": "No se pudo registrar el Movimiento"
        }), 400  
from flask import jsonify, request
from app import app
from app.services.cuenta_service import CuentaService
from app.models.cuenta import Cuenta

@app.route("/cuenta", methods=['GET'])
def cuenta():
    """
    Obtener una cuenta por su número de cuenta.

    ---
    tags:
      - Cuentas
    parameters:
      - in: query
        name: numero_cuenta
        schema:
          type: string
        required: true
        description: Número de cuenta a buscar.
    responses:
      200:
        description: Retorna la cuenta encontrada.
        content:
          application/json:
            schema:
              type: object
              properties:
                numero_cuenta:
                  type: string
                  description: El número de la cuenta.
                tipo_cuenta:
                  type: string
                  description: El tipo de cuenta (e.g., ahorros, corriente).
                saldo_cuenta:
                  type: number
                  format: float
                  description: El saldo actual de la cuenta.
                id_usuario:
                  type: integer
                  description: El ID del usuario asociado con la cuenta.
      400:
        description: Solicitud inválida, número de cuenta no proporcionado.
      404:
        description: Cuenta no encontrada.
    """
    data = request.get_json()
    numero_cuenta = data.get("numero_cuenta")
    rows = CuentaService.obtener_cuenta(numero_cuenta)
    cuenta = [cuenta.as_dict() for cuenta in rows]
    return jsonify(cuenta)


@app.route("/cuentas", methods=['GET'])
def cuentas():
    """
    Obtener todas las cuentas disponibles.

    ---
    tags:
      - Cuentas
    responses:
      200:
        description: Retorna todas las cuentas disponibles.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  numero_cuenta:
                    type: string
                    description: El número de la cuenta.
                  tipo_cuenta:
                    type: string
                    description: El tipo de cuenta (e.g., ahorros, corriente).
                  saldo_cuenta:
                    type: number
                    format: float
                    description: El saldo actual de la cuenta.
                  id_usuario:
                    type: integer
                    description: El ID del usuario asociado con la cuenta.
    """
    rows = CuentaService.obtener_cuentas()
    cuentas = [cuentas.as_dict() for cuentas in rows]
    return jsonify(cuentas)

@app.route("/cuenta", methods=['POST'])
def cuenta_r():
    """
    Crear una nueva cuenta.

    ---
    tags:
      - Cuentas
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              numero_cuenta:
                type: string
                example: "1234567890"
                description: El número de cuenta.
              tipo_cuenta:
                type: string
                example: "corriente"
                description: El tipo de cuenta (e.g., ahorros, corriente).
              saldo_cuenta:
                type: number
                example: 1000.0
                format: float
                description: El saldo inicial de la cuenta.
              id_usuario:
                type: integer
                example: 1
                description: El ID del usuario asociado con la cuenta.
    responses:
      200:
        description: Retorna la cuenta creada exitosamente.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "Cuenta ingresada exitosamente"
                cuenta:
                  type: object
                  properties:
                    numero_cuenta:
                      type: string
                      description: El número de la cuenta.
                    tipo_cuenta:
                      type: string
                      description: El tipo de cuenta (e.g., ahorros, corriente).
                    saldo_cuenta:
                      type: number
                      format: float
                      description: El saldo actual de la cuenta.
                    id_usuario:
                      type: integer
                      description: El ID del usuario asociado con la cuenta.
      400:
        description: Error al crear la cuenta.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "No se pudo crear la Cuenta"
    """
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
    

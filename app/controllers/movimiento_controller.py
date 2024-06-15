from flask import jsonify, request
from app import app
from app.services.movimiento_service import MovimientoService

@app.route("/movimiento", methods=['GET'])
def movimiento():
    """
    Obtener movimientos por número de cuenta.

    ---
    tags:
      - Movimientos
    parameters:
      - in: query
        name: numero_cuenta
        schema:
          type: string
        required: true
        description: Número de cuenta para filtrar movimientos.
    responses:
      200:
        description: Retorna los movimientos encontrados.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  tipo_movimiento:
                    type: string
                    description: Tipo de movimiento (e.g., depósito, retiro).
                  numero_cuenta:
                    type: string
                    description: Número de cuenta asociado al movimiento.
      400:
        description: Solicitud inválida, número de cuenta no proporcionado.
    """
    data = request.get_json()
    numero_cuenta = data.get("numero_cuenta")
    rows = MovimientoService.obtener_movimiento(numero_cuenta)
    movimiento = [movimiento.as_dict() for movimiento in rows]
    return jsonify(movimiento)

@app.route("/movimientos", methods=['GET'])
def movimientos():
    """
    Obtener todos los movimientos disponibles.

    ---
    tags:
      - Movimientos
    responses:
      200:
        description: Retorna todos los movimientos disponibles.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  tipo_movimiento:
                    type: string
                    description: Tipo de movimiento (e.g., depósito, retiro).
                  numero_cuenta:
                    type: string
                    description: Número de cuenta asociado al movimiento.
    """
    rows = MovimientoService.obtener_usuarios()
    movimientos = [movimientos.as_dict() for movimientos in rows]
    return jsonify(movimientos)

@app.route("/movimiento", methods=['POST'])
def movimiento_r():
    """
    Crear un nuevo movimiento.

    ---
    tags:
      - Movimientos
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              tipo_movimiento:
                type: string
                example: "depósito"
                description: Tipo de movimiento (e.g., depósito, retiro).
              numero_cuenta:
                type: string
                example: "1234567890"
                description: Número de cuenta asociado al movimiento.
    responses:
      200:
        description: Retorna el movimiento creado exitosamente.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "Movimiento ingresado exitosamente"
                movimiento:
                  type: object
                  properties:
                    tipo_movimiento:
                      type: string
                      description: Tipo de movimiento.
                    numero_cuenta:
                      type: string
                      description: Número de cuenta asociado al movimiento.
      400:
        description: Error al crear el movimiento.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "No se pudo registrar el Movimiento"
    """
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
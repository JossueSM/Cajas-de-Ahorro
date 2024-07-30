from flask import jsonify, request
from app import app
from app.services.reporte_service import ReporteService

@app.route("/reporte", methods=['GET'])
def reporte():
    """
    Obtener reportes por ID de usuario.

    ---
    tags:
      - Reportes
    parameters:
      - in: query
        name: id_usuario
        schema:
          type: string
        required: true
        description: ID del usuario para filtrar reportes.
    responses:
      200:
        description: Retorna los reportes encontrados.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id_reporte:
                    type: integer
                    description: ID del reporte.
                  id_usuario:
                    type: string
                    description: ID del usuario asociado al reporte.
                  id_movimiento:
                    type: string
                    description: ID del movimiento asociado al reporte.
                  description_reporte:
                    type: string
                    description: Descripción del reporte.
      400:
        description: Solicitud inválida, ID de usuario no proporcionado.
    """
    data = request.get_json()
    id_usuario = str(data.get("id_usuario"))
    rows = ReporteService.obtener_reporte_por_usuario(id_usuario)
    reportes = [reporte.as_dict() for reporte in rows]
    return jsonify(reportes)

@app.route("/reporte", methods=['POST'])
def ingresar_reporte():
    """
    Ingresar un nuevo reporte.

    ---
    tags:
      - Reportes
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              id_usuario:
                type: string
                example: "1"
                description: ID del usuario asociado al reporte.
              id_movimiento:
                type: string
                example: "1"
                description: ID del movimiento asociado al reporte.
              description_reporte:
                type: string
                example: "Reporte de error en la transacción."
                description: Descripción del reporte.
    responses:
      200:
        description: Retorna el reporte ingresado exitosamente.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "Reporte ingresado exitosamente"
                reporte:
                  type: object
                  properties:
                    id_reporte:
                      type: integer
                      description: ID del reporte.
                    id_usuario:
                      type: string
                      description: ID del usuario asociado al reporte.
                    id_movimiento:
                      type: string
                      description: ID del movimiento asociado al reporte.
                    description_reporte:
                      type: string
                      description: Descripción del reporte.
      400:
        description: Error al ingresar el reporte.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "No se pudo ingresar el Reporte"
    """
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    id_movimiento = data.get("id_movimiento")
    description_reporte = data.get("description_reporte")

    nuevo_reporte = ReporteService.ingresar_reporte(id_usuario, id_movimiento, description_reporte)

    return jsonify({
        "mensaje": "Reporte ingresado exitosamente",
        "reporte": {
            "id_reporte": nuevo_reporte.id_reporte,
            "id_usuario": nuevo_reporte.id_usuario,
            "id_movimiento": nuevo_reporte.id_movimiento,
            "description_reporte": nuevo_reporte.description_reporte
        }
    })
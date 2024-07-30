from flask import jsonify, request
from app import app
from app.services.socio_service import SocioService

@app.route("/socio", methods=['GET'])
def socio():
    """
    Obtener información de un socio por ID de usuario.

    ---
    tags:
      - Socios
    parameters:
      - in: query
        name: id_usuario
        schema:
          type: string
        required: true
        description: ID del usuario para buscar su información de socio.
    responses:
      200:
        description: Retorna la información del socio encontrada.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id_usuario:
                    type: string
                    description: ID del usuario asociado al socio.
                  estado_socio:
                    type: string
                    description: Estado del socio (e.g., activo, inactivo).
      400:
        description: Solicitud inválida, ID de usuario no proporcionado.
    """
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    rows = SocioService.obtener_socio(id_usuario)
    usuario = [usuario.as_dict() for usuario in rows]
    return jsonify(usuario)

@app.route("/socios", methods=['GET'])
def socios():
    """
    Obtener todos los socios registrados.

    ---
    tags:
      - Socios
    responses:
      200:
        description: Retorna todos los socios registrados.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id_usuario:
                    type: string
                    description: ID del usuario asociado al socio.
                  estado_socio:
                    type: string
                    description: Estado del socio (e.g., activo, inactivo).
    """
    rows = SocioService.obtener_socios()
    socios = [socios.as_dict() for socios in rows]
    return jsonify(socios)

@app.route("/socio", methods=['POST'])
def socio_r():
    """
    Crear un nuevo socio.

    ---
    tags:
      - Socios
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
                description: ID del usuario asociado al nuevo socio.
              estado_socio:
                type: string
                example: "activo"
                description: Estado del socio (e.g., activo, inactivo).
    responses:
      200:
        description: Retorna el socio creado exitosamente.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "Socio ingresado exitosamente"
                Socio:
                  type: object
                  properties:
                    id_usuario:
                      type: string
                      description: ID del usuario asociado al socio.
                    estado_socio:
                      type: string
                      description: Estado del socio.
      400:
        description: Error al crear el socio.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "No se pudo crear el Socio"
    """
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    estado_socio = data.get("estado_socio")

    nuevo_socio = SocioService.crear_socio(id_usuario, estado_socio)

    if nuevo_socio:
        return jsonify({
            "mensaje": "Socio ingresado exitosamente",
            "Socio": {
                "id_usuario": nuevo_socio.id_usuario,
                "estado_socio": nuevo_socio.estado_socio
            }
        })
    else:
        return jsonify({
            "mensaje": "No se pudo crear el usuario"
        }), 400  
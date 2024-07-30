from flask import jsonify, request
from app import app
from app.services.usuario_service import UsuarioService

@app.route("/usuario", methods=['GET'])
def usuario():
    """
    Obtener información de un usuario por ID de usuario.

    ---
    tags:
      - Usuarios
    parameters:
      - in: query
        name: id_usuario
        schema:
          type: string
        required: true
        description: ID del usuario para buscar su información.
    responses:
      200:
        description: Retorna la información del usuario encontrada.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id_usuario:
                    type: string
                    description: ID del usuario.
                  nombre_usuario:
                    type: string
                    description: Nombre del usuario.
                  email_usuario:
                    type: string
                    description: Email del usuario.
                  password_usuario:
                    type: string
                    description: Contraseña del usuario (puede estar omitida por seguridad).
      400:
        description: Solicitud inválida, ID de usuario no proporcionado.
    """
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    rows = UsuarioService.obtener_usuario(id_usuario)
    usuario = [usuario.as_dict() for usuario in rows]
    return jsonify(usuario)

@app.route("/usuarios", methods=['GET'])
def usuarios():
    """
    Obtener todos los usuarios registrados.

    ---
    tags:
      - Usuarios
    responses:
      200:
        description: Retorna todos los usuarios registrados.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id_usuario:
                    type: string
                    description: ID del usuario.
                  nombre_usuario:
                    type: string
                    description: Nombre del usuario.
                  email_usuario:
                    type: string
                    description: Email del usuario.
                  password_usuario:
                    type: string
                    description: Contraseña del usuario (puede estar omitida por seguridad).
    """
    rows = UsuarioService.obtener_usuarios()
    usuarios = [usuarios.as_dict() for usuarios in rows]
    return jsonify(usuarios)

@app.route("/usuario", methods=['POST'])
def usuario_r():
    """
    Crear un nuevo usuario.

    ---
    tags:
      - Usuarios
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
                description: ID del nuevo usuario.
              nombre_usuario:
                type: string
                example: "usuario123"
                description: Nombre del nuevo usuario.
              email_usuario:
                type: string
                example: "usuario@example.com"
                description: Email del nuevo usuario.
              password_usuario:
                type: string
                example: "password123"
                description: Contraseña del nuevo usuario.
    responses:
      200:
        description: Retorna el usuario creado exitosamente.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "Usuario ingresado exitosamente"
                Usuario:
                  type: object
                  properties:
                    id_usuario:
                      type: string
                      description: ID del usuario.
                    nombre_usuario:
                      type: string
                      description: Nombre del usuario.
                    email_usuario:
                      type: string
                      description: Email del usuario.
                    password_usuario:
                      type: string
                      description: Contraseña del usuario (puede estar omitida por seguridad).
      400:
        description: Error al crear el usuario.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "No se pudo crear el usuario"
    """
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    nombre_usuario = data.get("nombre_usuario")
    email_usuario = data.get("email_usuario")
    password_usuario = data.get("password_usuario")

    # Assuming UsuarioService.crear_usuario() returns an object with attributes
    nuevo_usuario = UsuarioService.crear_usuario(id_usuario, nombre_usuario, email_usuario, password_usuario)

    if nuevo_usuario:
        return jsonify({
            "mensaje": "Usuario ingresado exitosamente",
            "Usuario": {
                "id_usuario": nuevo_usuario.id_usuario,
                "nombre_usuario": nuevo_usuario.nombre_usuario,
                "email_usuario": nuevo_usuario.email_usuario,
                "password_usuario": nuevo_usuario.password_usuario
            }
        })
    else:
        return jsonify({
            "mensaje": "No se pudo crear el usuario"
        }), 400  # Example HTTP status code for bad request
    


@app.route("/usuario", methods=['PUT'])
def usuario_a():
    """
    Actualizar la contraseña de un usuario por ID de usuario.

    ---
    tags:
      - Usuarios
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
                description: ID del usuario para actualizar su contraseña.
              password_usuario:
                type: string
                example: "nuevaclave123"
                description: Nueva contraseña del usuario.
    responses:
      200:
        description: Retorna la contraseña del usuario actualizada exitosamente.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "Clave de Usuario actualizado exitosamente"
                Usuario:
                  type: object
                  properties:
                    nombre_usuario:
                      type: string
                      description: Nombre del usuario.
      400:
        description: Error al actualizar la contraseña del usuario.
        content:
          application/json:
            schema:
              type: object
              properties:
                mensaje:
                  type: string
                  example: "No se pudo actualizar la clave del usuario"
    """
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    password_usuario = data.get("password_usuario")
    try:
        actualizar_usuario = UsuarioService.actualizar_usuario(id_usuario, password_usuario)
        if actualizar_usuario:
            return jsonify({
                "mensaje": "Clave de Usuario actualizado exitosamente",
                "Usuario": {
                    "nombre_usuario": actualizar_usuario.nombre_usuario
                }
            })
        else:
            return jsonify({
                "mensaje": "No se pudo actualizar la clave del usuario"
        }), 400  


    except:
        return jsonify({
                "mensaje": "Error en la Base de Datos"
        }), 400 

    

    
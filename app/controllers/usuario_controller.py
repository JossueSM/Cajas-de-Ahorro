from flask import jsonify, request
from app import app
from app.services.usuario_service import UsuarioService

@app.route("/usuario", methods=['GET'])
def usuario():
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    rows = UsuarioService.obtener_usuario(id_usuario)
    usuario = [usuario.as_dict() for usuario in rows]
    return jsonify(usuario)

@app.route("/usuarios", methods=['GET'])
def usuarios():
    rows = UsuarioService.obtener_usuarios()
    usuarios = [usuarios.as_dict() for usuarios in rows]
    return jsonify(usuarios)

@app.route("/usuario", methods=['POST'])
def usuario_r():
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

    

    
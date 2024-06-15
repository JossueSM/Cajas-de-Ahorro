from flask import jsonify, request
from app import app
from app.services.socio_service import SocioService

@app.route("/socio", methods=['GET'])
def socio():
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    rows = SocioService.obtener_socio(id_usuario)
    usuario = [usuario.as_dict() for usuario in rows]
    return jsonify(usuario)

@app.route("/socios", methods=['GET'])
def socios():
    rows = SocioService.obtener_socios()
    socios = [socios.as_dict() for socios in rows]
    return jsonify(socios)

@app.route("/socio", methods=['POST'])
def socio_r():
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
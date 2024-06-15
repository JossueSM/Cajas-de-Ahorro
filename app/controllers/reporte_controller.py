from flask import jsonify, request
from app import app
from app.services.reporte_service import ReporteService

@app.route("/reporte", methods=['GET'])
def reporte():
    data = request.get_json()
    id_usuario = str(data.get("id_usuario"))
    rows = ReporteService.obtener_reporte_por_usuario(id_usuario)
    reportes = [reporte.as_dict() for reporte in rows]
    return jsonify(reportes)

@app.route("/reporte", methods=['POST'])
def ingresar_reporte():
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
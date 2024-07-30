from app import db
from app.models.reporte_cuenta import ReporteCuenta

class ReporteRepository:
    @staticmethod
    def obtener_reporte_por_usuario(id_usuario):
        return ReporteCuenta.query.filter_by(id_usuario=id_usuario).all()

    @staticmethod
    def crear_reporte(id_usuario, id_movimiento, description_reporte):
        nuevo_reporte = ReporteCuenta(
            id_usuario=id_usuario,
            id_movimiento=id_movimiento,
            description_reporte=description_reporte
        )
        db.session.add(nuevo_reporte)
        db.session.commit()
        return nuevo_reporte

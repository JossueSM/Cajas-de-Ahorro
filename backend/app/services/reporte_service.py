from app.repositories.reporte_repository import ReporteRepository
class ReporteService:
    @staticmethod
    def obtener_reporte_por_usuario(id_usuario):
        return ReporteRepository.obtener_reporte_por_usuario(id_usuario)

    @staticmethod
    def ingresar_reporte(id_usuario, id_movimiento, description_reporte):
        return ReporteRepository.crear_reporte(id_usuario, id_movimiento, description_reporte)
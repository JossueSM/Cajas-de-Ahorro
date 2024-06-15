from app.repositories.socio_repository import SocioRepository
class SocioService:
    @staticmethod
    def obtener_socio(id_usuario):
        return SocioRepository.obtener_socio(id_usuario)
    
    @staticmethod
    def obtener_socios():
        return SocioRepository.obtener_socios()

    @staticmethod
    def crear_socio(id_usuario, estado_socio):
        return SocioRepository.crear_socio(id_usuario, estado_socio)
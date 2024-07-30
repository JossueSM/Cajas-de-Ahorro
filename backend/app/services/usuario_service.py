from app.repositories.usuario_repository import UsuarioRepository
class UsuarioService:
    @staticmethod
    def obtener_usuario(id_usuario):
        return UsuarioRepository.obtener_usuario(id_usuario)
    
    @staticmethod
    def obtener_usuarios():
        return UsuarioRepository.obtener_usuarios()

    @staticmethod
    def crear_usuario(id_usuario, nombre_usuario, email_usuario,password_usuario):
        return UsuarioRepository.crear_usuario(id_usuario, nombre_usuario, email_usuario,password_usuario)
    
    @staticmethod
    def actualizar_usuario(id_usuario, password_usuario):
        return UsuarioRepository.actualizar_usuario(id_usuario, password_usuario)
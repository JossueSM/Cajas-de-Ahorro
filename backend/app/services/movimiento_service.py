from app.repositories.movimiento_repository import MovimientoRepository
class MovimientoService:
    @staticmethod
    def obtener_movimiento(numero_cuenta):
        return MovimientoRepository.obtener_movimiento(numero_cuenta)
    
    @staticmethod
    def obtener_usuarios():
        return MovimientoRepository.obtener_movimientos()

    @staticmethod
    def crear_movimiento(tipo_movimiento, numero_cuenta):
        return MovimientoRepository.crear_movimiento(tipo_movimiento, numero_cuenta)
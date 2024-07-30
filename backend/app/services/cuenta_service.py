from app.repositories.cuenta_repository import CuentaRepository
class CuentaService:
    @staticmethod
    def obtener_cuenta(numero_cuenta):
        return CuentaRepository.obtener_cuenta(numero_cuenta)
    
    @staticmethod
    def obtener_cuentas():
        return CuentaRepository.obtener_cuentas()

    @staticmethod
    def crear_cuenta(numero_cuenta,tipo_cuenta,saldo_cuenta,id_usuario):
        return CuentaRepository.crear_cuenta(numero_cuenta,tipo_cuenta,saldo_cuenta,id_usuario)
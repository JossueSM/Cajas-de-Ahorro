from app import db
from app.models.cuenta import Cuenta

class CuentaRepository:
    @staticmethod
    def obtener_cuenta(numero_cuenta):
        return Cuenta.query.filter_by(numero_cuenta=numero_cuenta).all()
    
    @staticmethod
    def obtener_cuentas():
        return Cuenta.query.all()

    @staticmethod
    def crear_cuenta(numero_cuenta,tipo_cuenta,saldo_cuenta,id_usuario):
        nueva_cuenta = Cuenta(
            numero_cuenta=numero_cuenta,
            tipo_cuenta=tipo_cuenta,
            saldo_cuenta=saldo_cuenta,
            id_usuario=id_usuario
        )
        db.session.add(nueva_cuenta)
        db.session.commit()
        return nueva_cuenta
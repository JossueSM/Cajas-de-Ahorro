from app import db
from app.models.movimiento import Movimiento

class MovimientoRepository:
    @staticmethod
    def obtener_movimiento(numero_cuenta):
        return Movimiento.query.filter_by(numero_cuenta=numero_cuenta).all()
    
    @staticmethod
    def obtener_movimientos():
        return Movimiento.query.all()

    @staticmethod
    def crear_movimiento(tipo_movimiento, numero_cuenta):
        nuevo_movimiento = Movimiento(
            tipo_movimiento=tipo_movimiento,
            numero_cuenta=numero_cuenta,
        )
        db.session.add(nuevo_movimiento)
        db.session.commit()
        return nuevo_movimiento

from app import db

class Movimiento(db.Model):
    __tablename__ = 'movimiento'

    id_movimiento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_movimiento = db.Column(db.String, nullable=False)
    numero_cuenta = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Movimiento {self.id_movimiento}>'
    
    def as_dict(self):
        return {
            "id_movimiento": self.id_movimiento,
            "tipo_movimiento": self.tipo_movimiento,
            "numero_cuenta": self.numero_cuenta
        }

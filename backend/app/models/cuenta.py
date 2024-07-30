from app import db

class Cuenta(db.Model):
    __tablename__ = 'cuenta'

    numero_cuenta = db.Column(db.String, primary_key=True)
    tipo_cuenta = db.Column(db.String, nullable=False)
    saldo_cuenta = db.Column(db.Double, nullable=False)
    id_usuario = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Cuenta {self.numero_cuenta}>'
    
    def as_dict(self):
        return {
            "numero_cuenta": self.numero_cuenta,
            "tipo_cuenta": self.tipo_cuenta,
            "saldo_cuenta": self.saldo_cuenta,
            "id_usuario": self.id_usuario
        }
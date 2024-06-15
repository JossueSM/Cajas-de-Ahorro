from app import db

class Socio(db.Model):
    __tablename__ = 'socio'

    id_socio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.String(10), nullable=False)
    estado_socio = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        return f'<Socio {self.id_socio}>'
    
    def as_dict(self):
        return {
            "id_socio": self.id_socio,
            "id_usuario": self.id_usuario,
            "estado_socio": self.estado_socio
        }
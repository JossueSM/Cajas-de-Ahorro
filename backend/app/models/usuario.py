from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.String(10), primary_key=True)
    nombre_usuario = db.Column(db.String(), nullable=False)
    email_usuario = db.Column(db.String(), nullable=False, unique=True)
    password_usuario = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.id_usuario}>'
    
    def as_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "email_usuario": self.email_usuario,
            "password_usuario": self.password_usuario
        }
from app import db
from app.models.socio import Socio

class SocioRepository:
    @staticmethod
    def obtener_socio(id_usuario):
        return Socio.query.filter_by(id_usuario=id_usuario).all()
    
    @staticmethod
    def obtener_socios():
        return Socio.query.all()

    @staticmethod
    def crear_socio(id_usuario, estado_socio):
        nuevo_socio = Socio(
            id_usuario=id_usuario,
            estado_socio = estado_socio
        )
        db.session.add(nuevo_socio)
        db.session.commit()
        return nuevo_socio

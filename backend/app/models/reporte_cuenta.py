from app import db

class ReporteCuenta(db.Model):
    __tablename__ = 'reporte_cuenta'

    id_reporte = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.String(10), nullable=False)
    id_movimiento = db.Column(db.Integer, nullable=False)
    description_reporte = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<ReporteCuenta {self.id_reporte}>'

    def as_dict(self):
        return {
            "id_reporte": self.id_reporte,
            "id_usuario": self.id_usuario,
            "id_movimiento": self.id_movimiento,
            "description_reporte": self.description_reporte
        }
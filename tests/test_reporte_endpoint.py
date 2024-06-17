import json
from flask_testing import TestCase
from config import TestConfig, Config
from app import app, db

class TestFlaskRoutes(TestCase):
    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        db.create_all()  # Crea las tablas necesarias para la prueba

    def tearDown(self):
        db.session.remove()
        # db.drop_all()  # Elimina todas las tablas al finalizar la prueba

    def test_crear_reporte(self):
        # Prueba de la creación de una cuenta
        response = self.client.post("/reporte", data=json.dumps({
            "description_reporte": "Reporte exitoso",
            "id_movimiento": 1,
            "id_usuario": "1"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Reporte', response.json['mensaje'])
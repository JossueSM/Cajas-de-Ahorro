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

    def test_crear_movimiento(self):
        # Prueba de la creación de una cuenta
        response = self.client.post("/movimiento", data=json.dumps({
            "numero_cuenta": "12345",
            "tipo_movimiento": "deposito"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Movimiento", response.json['mensaje'])

    def test_obtener_movimiento(self):
        response = self.client.get("/movimiento", data=json.dumps({"numero_cuenta": "12345"}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("tipo_movimiento", response.json[0])

    def test_movimientos(self):
        response = self.client.get("/movimientos")
        self.assertEqual(response.status_code, 200)
        self.assertIn("tipo_movimiento", response.json[0])
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

    def test_crear_cuenta(self):
        # Prueba de la creación de una cuenta
        response = self.client.post("/cuenta", data=json.dumps({
            "numero_cuenta": "12345",
            "tipo_cuenta": "Ahorro",
            "saldo_cuenta": 1000.0,
            "id_usuario": 1
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Cuenta ingresada exitosamente', response.json['mensaje'])

    def test_obtener_cuenta(self):
        response = self.client.get("/cuenta", data=json.dumps({"numero_cuenta": "12345"}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('saldo_cuenta', response.json[0])

    def test_cuentas(self):
        response = self.client.get("/cuentas")
        self.assertEqual(response.status_code, 200)
        self.assertIn('saldo_cuenta', response.json[0])
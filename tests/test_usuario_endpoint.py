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

    def test_crear_socio(self):
        # Prueba de la creación de una cuenta
        response = self.client.post("/usuario", data=json.dumps({
            "id_usuario": "1",
            "nombre_usuario": "Jossue",
            "email_usuario": "jsimancasm@est.ups.edu.ec",
            "password_usuario": "123"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Usuario', response.json['mensaje'])
    
    def test_obtener_usuario(self):
        response = self.client.get("/usuario", data=json.dumps({"id_usuario": "1"}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('email_usuario', response.json[0])
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
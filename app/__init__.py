from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita warnings

db = SQLAlchemy(app)
CORS(app)

# Importa los controladores después de inicializar db para evitar problemas circulares
from app.controllers import cuenta_controller
from app.controllers import movimiento_controller
from app.controllers import reporte_controller
from app.controllers import socio_controller


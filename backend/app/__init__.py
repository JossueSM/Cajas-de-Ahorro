from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import TestConfig, Config
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
CORS(app)
swagger = Swagger(app)

# Importa los controladores después de inicializar db para evitar problemas circulares
from app.controllers import cuenta_controller
from app.controllers import movimiento_controller
from app.controllers import reporte_controller
from app.controllers import socio_controller
from app.controllers import usuario_controller


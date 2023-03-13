from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('proformas', __name__)
cors = CORS(bp,resources={r"/*": {"origins": "*", "headers":["Content-Type", "Authorization"]}})

# from app.login import routes
from app.proformas.rutas import cabecera_por_numped
from app.proformas.rutas import detalle_por_numped
from app.proformas.rutas import nuevaCabecera
from app.proformas.rutas import updateCabecera

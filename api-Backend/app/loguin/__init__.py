from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('loguin', __name__)
cors = CORS(bp,resources={r"/*": {"origins": "*", "headers":["Content-Type", "Authorization"]}})

from app.loguin import routes
from app.loguin.rutas import buscar_cliciausu
from app.loguin.rutas import usuario_existe
from app.loguin.rutas import companias_del_usuario
from app.loguin.rutas import inicio_sesion
from app.loguin.rutas import get_localidad
from app.loguin.rutas import get_menu


# from app.loguin.rutas import ruta_aparte
# from app.loguin.rutas import *
# import app.loguin.rutas
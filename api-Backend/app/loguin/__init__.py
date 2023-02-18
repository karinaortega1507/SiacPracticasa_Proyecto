from flask import Blueprint

bp = Blueprint('loguin', __name__)


from app.loguin import routes
from app.loguin.rutas import buscar_cliciausu
from app.loguin.rutas import usuario_existe
from app.loguin.rutas import companias_del_usuario


# from app.loguin.rutas import ruta_aparte
# from app.loguin.rutas import *
# import app.loguin.rutas
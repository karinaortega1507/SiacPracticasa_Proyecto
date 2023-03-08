from flask import jsonify, request
from app.proformas import bp
from app.extensions import db
from flask_cors import cross_origin
from app.models.Cabecera import Cabecera, CabeceraSchema
from app.models.Detalle import Detalle, DetalleSchema


# recive esta estructura
# {
#   "numped": "numped"
# }
@bp.route('/cabecera_por_numped', methods=['POST'])
@cross_origin()
def Cabecera_por_numped():
    # Obtener el JSON enviado en la solicitud
    data = request.get_json()
    # Obtener el valor de "numped" del JSON
    numped = data['numped']

    # Obtener la cabecera con el numped
    cabecera = Cabecera.query.filter_by(pednumped=numped).first()

    if cabecera:
        # Serializar los resultados usando el esquema
        result_cabecera = CabeceraSchema().dump(cabecera)

        # Devolver una respuesta con el estado "ok" y los datos de la cabecera
        response = {
            'status': 'ok',
            'data': result_cabecera
        }
    else:
        # Si no se encontró un registro, devolver una respuesta con el estado "error"
        response = {
            'status': 'error',
            'message': 'No se encontró ningún registro con numped = {}'.format(numped)
        }

    # Devolver la respuesta en formato JSON
    return jsonify(response)


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
@bp.route('/detalle_por_numped', methods=['POST'])
@cross_origin()
def Detalle_por_numped():
    # Obtener el JSON enviado en la solicitud
    data = request.get_json()
    # Obtener el valor de "numped" del JSON
    numped = data['numped']

    # Obtener la detalle con el numped
    detalle = Detalle.query.filter_by(pednumped=numped).first()

    if detalle:
        # Serializar los resultados usando el esquema
        result_detalle = DetalleSchema().dump(detalle)

        # Devolver una respuesta con el estado "ok" y los datos de la Detalle
        response = {
            'status': 'ok',
            'data': result_detalle
        }
    else:
        # Si no se encontró un detalle, devolver una respuesta con el estado "error"
        response = {
            'status': 'error',
            'message': 'No se encontró ningún detalle con numped = {}'.format(numped)
        }

    # Devolver la respuesta en formato JSON
    return jsonify(response)


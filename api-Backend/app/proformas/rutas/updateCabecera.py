from datetime import datetime
import json
from flask import jsonify, request
from app.proformas import bp
from app.extensions import db
from flask_cors import cross_origin
from app.models.Cabecera import Cabecera, CabeceraSchema
from app.models.Detalle import Detalle, DetalleSchema
from app.models.fapvendedor import Fapvendedor, FapvendedorSchema
from app.models.cxcmcli import Cxcmcli, CxcmcliSchema
from app.models.SiacSys import SiacSys, SiacSysSchema

# recive esta estructura
# {
#   "user": "user",
#   "numped": "numped",
#   "pedtivapor": "pedtivapor",
#   "pedsubtot": "pedsubtot",
#   "pediva": "pediva",
#   "pedtotal": "pedtotal",
#   "pedusuisys": "pedusuisys",
#   "ciacodigo": "ciacodigo",
#   "loccodigo": "loccodigo",
#   "pedvalser": "pedvalser",
#   "mesacodigo": "mesacodigo",
# }
# @bp.route('/actualizarCabecera/<numped>', methods=['PUT'])
@bp.route('/updateCabecera', methods=['post'])
@cross_origin()
def actualizarCabecera():
    data = request.json
    numped = data['numped']
    ciacodigo = data['ciacodigo']

    cabecera = Cabecera.query.filter_by(pednumped=numped, ciacodigo=ciacodigo).first()
    if cabecera is None:
        return jsonify({'error': f'No se encontró ninguna cabecera con numped {numped}'}), 404

    cabecera.user       =   data['user']
    cabecera.pedtivapor =   data['pedtivapor']
    cabecera.pedsubtot  =   data['pedsubtot']
    cabecera.pediva     =   data['pediva']
    cabecera.pedtotal   =   data['pedtotal']
    cabecera.pedusuisys =   data['pedusuisys']
    cabecera.ciacodigo  =   data['ciacodigo']
    cabecera.loccodigo  =   data['loccodigo']
    cabecera.pedvalser  =   data['pedvalser']
    cabecera.mesacodigo =   data['mesacodigo']

    # cabecera.user = data.get('user', cabecera.user)
    # cabecera.pedtivapor = data.get('pedtivapor', cabecera.pedtivapor)
    # cabecera.pedsubtot = data.get('pedsubtot', cabecera.pedsubtot)
    # cabecera.pediva = data.get('pediva', cabecera.pediva)
    # cabecera.pedtotal = data.get('pedtotal', cabecera.pedtotal)
    # cabecera.pedusuisys = data.get('pedusuisys', cabecera.pedusuisys)
    # cabecera.ciacodigo = data.get('ciacodigo', cabecera.ciacodigo)
    # cabecera.loccodigo = data.get('loccodigo', cabecera.loccodigo)
    # cabecera.pedvalser = data.get('pedvalser', cabecera.pedvalser)
    # cabecera.mesacodigo = data.get('mesacodigo', cabecera.mesacodigo)

    db.session.commit()

    return jsonify({'message': f'Cabecera con numped {numped} actualizada exitosamente'})

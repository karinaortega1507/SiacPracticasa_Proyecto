from datetime import datetime
import json
from flask import jsonify, request
from app.models.Detalle import Detalle
from app.proformas import bp
from app.extensions import db
from flask_cors import cross_origin
# recive esta estructura:
# {
    # "user": "user",
#   "ciacodigo": "ciacodigo",
#   "pednumped": "pednumped",
#   "pedsecuen": "pedsecuen",
#   "facnumfac": "facnumfac",
#   "pedtipo": "pedtipo",
#   "pedapliiva": "pedapliiva",
#   "factippag": "factippag",
#   "moncodigo": "moncodigo",
# }

@bp.route('/updateDetalle', methods=['POST'])
@cross_origin()
def updateDetalle():
    data = request.json
    numped = data['numped']
    ciacodigo = data['ciacodigo']

    detalle = Detalle.query.filter_by(pednumped=numped, ciacodigo=ciacodigo).first()
    if detalle is None:
        return jsonify({'error': f'No se encontró ninguna detalle con numped {numped}'}), 404

    # detalle.ciacodigo = data["ciacodigo"],
    # detalle.pednumped = data["pednumped"],
    detalle.pedsecuen = data["pedsecuen"],
    detalle.facnumfac = data["facnumfac"],
    detalle.pedtipo = data["pedtipo"],
    detalle.pedapliiva = data["pedapliiva"],
    detalle.factippag = data["factippag"],
    detalle.moncodigo = data["moncodigo"],

    db.session.commit()

    return jsonify({'message': f'detalle con numped {numped} actualizada exitosamente'})

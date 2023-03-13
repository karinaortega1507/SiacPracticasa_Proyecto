from datetime import datetime
import json
from flask import jsonify, request
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
    # (select clicodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
    clicodigo = Cabecera.query.filter_by(pednumped=data['pednumped']).first()

    # (select lincodigo from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    lincodigo = inmart.query.filter_by(artcodigo=data['artcodigo']).first()

    # (select vencodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
    vencodigo = Cabecera.query.filter_by(pednumped=data['pednumped']).first()

    # (select zoncodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
    zoncodigo = Cabecera.query.filter_by(pednumped=data['pednumped']).first()

    # (select artprecventa1 from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    artprecventa1 = inmart.query.filter_by(artcodigo=data['artcodigo']).first()
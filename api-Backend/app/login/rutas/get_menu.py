from flask import jsonify, request
from sqlalchemy import text
from app.login import bp
from app.extensions import db
from flask_cors import cross_origin

from app.models.siacopc import Siacopc, SiacopcSchema
from app.models.siactusrweb import Siactusrweb


# {
#     "user": "­v}xg",
#     "password": "I4bªszuj",
#     "seleccion": 
#         {
#             "cliciaciacodigo": "01",
#             "cliciacianombre": "PRACTICASA",
#             "clicianonBD": "SiacPracticasa",
#             "cliciarutaBD": "fsoftapptest.futuresoft-ec.com,14666"
#         },
#     "localidad":
#         {
#             "loccodigo": "07",
#             "locdescri": "BODEGA SAMBO"
#         },
# }




@bp.route('/get_menu', methods=['POST'])
@cross_origin()
def get_menu():
    data = request.get_json()
    cliciaciacodigo = data['seleccion']['cliciaciacodigo']
    user = data['user']

    # resultado = db.session.query(Siacopc)\
    #     .join(Siactusrweb, (Siacopc.ciacodigo == Siactusrweb.ciacodigo) & (Siacopc.modcodigo == Siactusrweb.modcodigo))\
    #     .filter(Siactusrweb.ciacodigo == cliciaciacodigo, Siactusrweb.usrcodigo == user, Siactusrweb.modcodigo == 'WEB')\
    #     .order_by(Siacopc.opctag)\
    #     .all()
    # return jsonify(resultado)

    results = db.session.query(Siacopc.opctag,Siacopc.opccaption,Siacopc.nivel,Siacopc.item_number,Siacopc.padre_id)\
                    .join(Siactusrweb,
                    (Siacopc.opctag == Siactusrweb.opctag) &
                    (Siacopc.modcodigo == Siactusrweb.modcodigo))\
                    .filter(Siactusrweb.ciacodigo == cliciaciacodigo,
                         Siactusrweb.usrcodigo == user)\
                    .order_by(Siacopc.opctag)\
                    .all()
                         # Siactusrweb.modcodigo == 'WEB')\

    local_schema = SiacopcSchema(many=True)
    output = local_schema.dump(results)

    return jsonify(output)

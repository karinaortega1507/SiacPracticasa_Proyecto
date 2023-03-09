from flask import jsonify, request
from sqlalchemy import text
from app.login import bp
from app.extensions import db
from flask_cors import cross_origin
from app.models.Cgblocal import Cgblocal, CgblocalSchema
from app.models.DynamicLoginDB import DynamicLoginDB, DynamicLoginDBSchema
from app.models.Siactloc import Siactloc
from app.models.fsbsmcliusu import fsbsmcliusu, fsbsmcliusu_schema_varios, fsbsmcliusu_schema
from app.models.fsbsmclicia import fsbsmclicia, fsbsmclicia_schema_varios, fsbsmclicia_schema


# {
#   "user": "­v}xg",
#   "password": "I4bªszuj",
#   "seleccion": 
#       {
#           "cliciaciacodigo": "01",
#           "cliciacianombre": "PRACTICASA",
#           "clicianonBD": "SiacPracticasa",
#           "cliciarutaBD": "fsoftapptest.futuresoft-ec.com,14666"
#       }
# }
@bp.route('/get_localidad', methods=['POST'])
@cross_origin()
def get_localidad():
    # Valida los datos del request
    request_data = request.get_json()
    # errors = RequestSchema().validate(request_data)
    # if errors:
    #     return {'message': 'Datos de request inválidos', 'errors': errors}, 400

    # Obtiene los datos necesarios para el query
    user = request_data['user']
    seleccion = request_data['seleccion']
    cliciaciacodigo =seleccion['cliciaciacodigo']

    # Ejecuta el query con los datos obtenidos
    # query = f'''
    #     select b.locdescri, b.loccodigo from {seleccion['clicianonBD']}.dbo.siactloc a
    #     inner join {seleccion['clicianonBD']}.dbo.cgblocal b on a.ciacodigo = b.ciacodigo and a.loccodigo = b.loccodigo
    #     where a.ciacodigo = '{seleccion['cliciaciacodigo']}' and usrcodigo = '{user}' and b.locstatus = 'A'
    # '''
    # query = text(f'''
    #     select b.locdescri, b.loccodigo from SiacPracticasa.dbo.siactloc.dbo.siactloc a
    #     inner join SiacPracticasa.dbo.siactloc.dbo.cgblocal b on a.ciacodigo = b.ciacodigo and a.loccodigo = b.loccodigo
    #     where a.ciacodigo = '{seleccion['cliciaciacodigo']}' and usrcodigo = '{user}' and b.locstatus = 'A'
    # ''')

    # user = request.args.get('user')
    # cia_codigo = request.args.get('cia_codigo', '02')

    # # Ejecución de la consulta
    results = db.session.query(Cgblocal.locdescri, Cgblocal.loccodigo) \
        .join(Siactloc, Siactloc.ciacodigo == Cgblocal.ciacodigo) \
        .filter(Siactloc.ciacodigo == cliciaciacodigo, Siactloc.usrcodigo == user, Cgblocal.locstatus == 'A') \
        .distinct() \
        .all()

    # Serialización de los resultados con Marshmallow
    # local_schema = CgblocalSchema()
    local_schema = CgblocalSchema(many=True)
    output = local_schema.dump(results)

    return jsonify(output)


    # query = text('''select b.locdescri, b.loccodigo from SiacPracticasa.dbo.siactloc a
    #      inner join SiacPracticasa.dbo.cgblocal b on a.ciacodigo = b.ciacodigo and a.loccodigo = b.loccodigo
    #      where a.ciacodigo = '01' and b.locstatus = 'A' ''')

    # result = db.session.execute(query)

    # result = db.session.execute(query).fetchall()

    # # Retorna los resultados
    # return {'result': [dict(row) for row in result]}
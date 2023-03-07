import json
from flask import jsonify, request
from app.loguin import bp
from app.extensions import db
from flask_cors import cross_origin
from app.models.DynamicLoguinDB import DynamicLoguinDB, DynamicLoguinDBSchema
from services.encrip_desencrip import encriptar, desencriptar
from app.models.fsbsmcliusu import fsbsmcliusu, fsbsmcliusu_schema_varios, fsbsmcliusu_schema
from app.models.fsbsmclicia import fsbsmclicia, fsbsmclicia_schema_varios, fsbsmclicia_schema
# from app.models.siacPracticasaSiacusr import siacPracticasaSiacusr, siacPracticasaSiacusr_schema_varios, siacPracticasaSiacusr_schema



#  recive esta estructura
# {
#   "user": "­v}xg",
#   "password": "I4bªszuj",
#   "seleccion": 
#       {
#           "cliciaciacodigo": "01",
#           "cliciacianombre": "PRACTICASA",
#           "clicianonBD": "SiacPracticasa",
#           "cliciarutaBD": "fsoftapptest.futuresoft-ec.com,14666"
#       },
# }
# deberia devolver el jWT para la autenticacion
# pero no se como hacerlo de momento, XD, bueno devuelde ok iniciaste sesion
@bp.route('/inicio_sesion', methods=['POST'])
@cross_origin()
def inicio_sesion():
    data = request.get_json()
    print(data)
    clicianonBD = data['seleccion']['clicianonBD']
    # schema = {'schema': f'{clicianonBD}.dbo'}
    DynamicLoguinDB.__table_args__["schema"] = f'{clicianonBD}.dbo'
    # print("DynamicLoguinDB.__table_args__", DynamicLoguinDB.__table_args__)
    usuario = data['user']
    password = data['password']

    #encripta usuario y clave
    usrcodigo=encriptar(usuario)
    usrclave =encriptar(password)
    print(usrclave, usrcodigo)
    result = DynamicLoguinDB.query.filter_by(usrcodigo=usrcodigo).first()
    dynamic_login_schema = DynamicLoguinDBSchema()

    tabla = dynamic_login_schema.jsonify(result)
    tabla_dict = json.loads(tabla.data)
    # usrcodigo = tabla_dict['usrcodigo']

    if tabla_dict["usrcodigo"] == usrcodigo and tabla_dict["usrclave"] == usrclave:
        response = {
            'status': 'ok',
            'message': 'Iniciaste sesion',
            'data': {
                "user": usuario,
                "seleccion": data['seleccion']
            },
        }
    else:
        response = {
            'status': 'error',
            'message': 'datos incorrectos'
        }
    
    return jsonify(response)


    # data = request.json
    # usrcodigo = data['user']
    # # usrcodigo = request.args.get('usrcodigo')
    # usrclave = data['password']
    # query = siacPracticasaSiacusr.query.filter_by(usrcodigo=usrcodigo, usrclave=usrclave).all()
    # # siaccusr_schema = SiaccUsrSchema(many=True)
    # result = siacPracticasaSiacusr_schema.dump(query)
    # return {"siaccusr": result}


    # data = request.json
    # clicianonBD = data['seleccion']['clicianonBD']
    # schema = {'schema': f'{clicianonBD}.dbo'}
    # # DynamicLoguinDB.__tablename__ = 'siaccusr'
    # DynamicLoguinDB.__table_args__ = schema
    # usrcodigo = data['user']
    # result = DynamicLoguinDB.query.filter_by(usrcodigo=usrcodigo).first()
    # dynamic_login_schema = DynamicLoguinDBSchema()
    # return dynamic_login_schema.jsonify(result)



# # Obtener los datos de la petición
#     data = request.get_json()

#     # Obtener los valores de usuario, password y seleccion
#     usuario = data['user']
#     password = data['password']
#     seleccion = data['seleccion']

#     # Obtener los valores necesarios de seleccion
#     cliciacianombre = seleccion['cliciacianombre']
#     dynamic_user_DB = seleccion['clicianonBD']
#     cliciarutaBD = seleccion['cliciarutaBD']

#     #asumo que usuario y contrasenia son validos

#     # Obtener el modelo y el esquema adecuados según el valor de dynamic_user_DB
#     modelo = db.get_bind(bind=dynamic_user_DB).metadata.tables['siaccusr'] #usrcodigo
#     # esquema = siacPracticasaSiacusr_schema()

#     # Ejecutar la consulta en la base de datos correspondiente
#     resultado = db.session.execute(modelo.select().where(modelo.c.usrcodigo == usuario))

#     # Serializar el resultado usando el esquema correspondiente
#     resultado_serializado = siacPracticasaSiacusr_schema.dump(resultado)

#     # Retornar la respuesta como un JSON
#     return jsonify(resultado_serializado)
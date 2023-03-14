import json
from flask import jsonify, request
from app.login import bp
from app.extensions import db
from flask_cors import cross_origin
from app.models.DynamicLoginDB import DynamicLoginDB, DynamicLoginDBSchema
from services.encrip_desencrip import encriptar, desencriptar
from app.models.fsbsmcliusu import fsbsmcliusu, fsbsmcliusu_schema_varios, fsbsmcliusu_schema
from app.models.fsbsmclicia import fsbsmclicia, fsbsmclicia_schema_varios, fsbsmclicia_schema
# from app.models.siacPracticasaSiacusr import siacPracticasaSiacusr, siacPracticasaSiacusr_schema_varios, siacPracticasaSiacusr_schema

#Authorization JWT
from flask_jwt_extended import create_access_token
from datetime import timedelta
import app


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
    # print(data)
    # clicianonBD = data['seleccion']['clicianonBD']
    # schema = {'schema': f'{clicianonBD}.dbo'}
    # DynamicLoginDB.__table_args__["schema"] = f'{clicianonBD}.dbo'
    # print("DynamicLoginDB.__table_args__", DynamicLoginDB.__table_args__)
    usuario = data['user']
    password = data['password']


    #encripta usuario y clave
    # -------------------------------------
    # usrcodigo=encriptar(usuario)
    # usrclave =encriptar(password)
    # TODO: descomentar las dos lineas de arriba y comentar las dos de abajo
    usrcodigo=usuario
    usrclave =password
    # -------------------------------------

    result = DynamicLoginDB.query.filter_by(usrcodigo=usrcodigo).first()
    dynamic_login_schema = DynamicLoginDBSchema()

    tabla = dynamic_login_schema.jsonify(result)
    tabla_dict = json.loads(tabla.data)
    # usrcodigo = tabla_dict['usrcodigo']

    
    if  tabla_dict["usrcodigo"] == usrcodigo and tabla_dict["usrclave"] == usrclave :

        #Generar un json web token para dar autorización
        payload = {
            'user': usuario
        }
        #JWT_SECRET:access_token.decode('UTF-8')_KEY es el password para encriptar el token 
        access_token = create_access_token(identity= data,expires_delta=timedelta(hours=1), additional_claims=payload)


        response = {
            'status': 'ok',
            'message': 'Iniciaste sesion',
            'data': {
                "user": usuario,
                "seleccion": data['seleccion']
            },
            'access_token':access_token
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
    # # DynamicLoginDB.__tablename__ = 'siaccusr'
    # DynamicLoginDB.__table_args__ = schema
    # usrcodigo = data['user']
    # result = DynamicLoginDB.query.filter_by(usrcodigo=usrcodigo).first()
    # dynamic_login_schema = DynamicLoginDBSchema()
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
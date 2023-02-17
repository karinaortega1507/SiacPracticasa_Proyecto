from flask import jsonify, request
from app.loguin import bp
from app.extensions import db
from app.models.fsbsmcliusu import fsbsmcliusu, fsbsmcliusu_schema_varios, fsbsmcliusu_schema
from app.models.fsbsmclicia import fsbsmclicia, fsbsmclicia_schema_varios, fsbsmclicia_schema


#  recive esta estructura
# {
#   "cliciausu": "id_usuario",
#   "cliciagrupo": "id_empresa"
# }
# devuelve codigo de compania, nombre de compania, ruta de la base de datos y nombre de la base de datos
@bp.route('/companias_del_usuario', methods=['POST'])
def companias_del_usuario():
    # Obtener el JSON enviado en la solicitud
    data = request.get_json()

    # Obtener el valor de "cliciausu" del JSON
    cliciausu = data.get('cliciausu')

    # Obtener el valor de "cliciagrupo" del JSON
    cliciagrupo = data.get('cliciagrupo')

    # hacer el query de cuando ya tienes el usuario si existe
    consulta = db.session.query(fsbsmclicia.cliciaciacodigo, fsbsmclicia.cliciacianombre, fsbsmclicia.cliciarutaBD, fsbsmclicia.clicianonBD)\
    .join(fsbsmcliusu, fsbsmcliusu.cliciaidenti == fsbsmclicia.cliciaidenti and fsbsmcliusu.cliciagrupo == fsbsmcliusu.cliciagrupo)\
    .filter(fsbsmcliusu.cliciausu == cliciausu, fsbsmcliusu.cliciagrupo == cliciagrupo)
    
    # Obtener los resultados de la consulta
    resultados = consulta.all()

    # Comprobar si se resultados no esta vacio
    if resultados:

        # Serializar los resultados usando el esquema
        datos = fsbsmclicia_schema_varios.dump(resultados)

        # si el join no hace match con una parte del esquema, asi se hace json de manera manual
        # datos = []
        # for resultado in resultados:
        #     datos.append({
        #         'cliciaciacodigo': resultado[0],
        #         'cliciacianombre': resultado[1],
        #         'cliciarutaBD': resultado[2],
        #         'clicianonBD': resultado[3]
        #     })

        # Devolver una respuesta con el estado "ok" y los datos del usuario y los grupos a los que pertenece
        response = {
            'status': 'ok',
            'data': datos
        }
    else:
        # Si no se encontró un registro, devolver una respuesta con el estado "error"
        response = {
            'status': 'error',
            'message': 'ha ocurrido un error con cliciausu = {}'.format(cliciausu)
        }


    # Devolver la respuesta en formato JSON
    return jsonify(response)
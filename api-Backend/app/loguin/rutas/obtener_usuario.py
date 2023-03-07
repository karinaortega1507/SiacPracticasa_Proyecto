from flask import jsonify, request
from app.loguin import bp
from app.extensions import db
from flask_cors import cross_origin
from services.encrip_desencrip import encriptar, desencriptar

from app.models.usuario import Usuario, UsuarioSchema


@bp.route('/obtener_usuario', methods=['POST'])
@cross_origin()
def obtener_usuario():
    data = request.get_json()
    print (data)
    codigo = data.get('usrcodigo')
    clave= data.get('usrclave')
    usrcodigo = encriptar(codigo)
    usrclave = encriptar(clave)
    results = db.session.query(Usuario.usrnombre.label('nombre_usuario'))\
                        .filter(Usuario.usrcodigo == usrcodigo and
                                Usuario.usrclave == usrclave)\
                                 .first()

    local_schema = UsuarioSchema(many=True)
    output = local_schema.dump(results)

    return jsonify(output)
from datetime import datetime
import json
from flask import jsonify, request
from app.models.Cabecera import Cabecera
from app.models.Detalle import Detalle
from app.models.inmart import inmart
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
@bp.route('/nuevoDetalle', methods=['POST'])
@cross_origin()
def nuevoDetalle():
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

    # TODO: preguntar aqui por la multiplcacion
    # (select (artprecventa1*0.12) * @pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    artprecventa1_12 = inmart.query.filter_by(artcodigo=data['artcodigo']).first()

    # (select (artprecventa1* @pedcantidad) from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    artprecventa1_pedcantidad = inmart.query.filter_by(artcodigo=data['artcodigo']).first()

    # (select ((artprecventa1*0.12) + artprecventa1)*@pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    artprecventa1_12_pedcantidad = inmart.query.filter_by(artcodigo=data['artcodigo']).first()

    # (select artdescri from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    artdescri = inmart.query.filter_by(artcodigo=data['artcodigo']).first()

    # (select mesacodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
    mesacodigo = Cabecera.query.filter_by(pednumped=data['pednumped']).first()

    hoy = datetime.now().strftime("%Y-%m-%d 00:00:00.%f")[:-3]
    hoy_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    _nuevoDetalle = Detalle(
        ciacodigo =	data['ciacodigo'],
        pednumped =	data['pednumped'],
        pedsecuen =	data['pedsecuen'],
        loccodigo =	None,
        facnumfac =	'PR',
        pedtipo =	-1,
        pedapliiva =	'EFE',
        factippag =	'D',
        moncodigo =	0.00,
        pedcambio =	hoy,
        pedfecemi =	clicodigo,
        clicodigo =	data['clicodigo'],
        cliprecio =	1,
        pedstatus =	data['pedstatus'],
        bodcodigo =	'',
        invcodigo =	'01',
        artcodigo =	data['artcodigo'],
        precodigo =	'01',
        coscodigo =	'',
        lincodigo =	lincodigo,
        vencodigo =	vencodigo,
        zoncodigo =	zoncodigo,
        sercodigo =	'',
        pedcantidad =	data['pedcantidad'],
        pedcosto =	0.000000,
        pedcostodol =	0.000000,
        pedpreven =	artprecventa1,
        pedvaldesglo =	0.000000,
        pedvaldesc =	0.000000,
        pedvalrec =	0.000000,
        pediva =	12.00,

        # TODO: preguntar aqui por la multiplcacion
        pedvaliva =	artprecventa1_12,
        pedvalor =	artprecventa1_pedcantidad,
        pedvaltot =	artprecventa1_12_pedcantidad,
        
        pedfecisys =	hoy,
        pedhorisys =	hoy_hora,
        pedusuisys =	data['pedusuisys'],
        pedestisys =	data['user'],
        pedfecmsys =	hoy,
        pedhormsys =	hoy_hora,
        pedusumsys =	data['pedusumsys'],
        pedestmsys =	data['user'],
        tipcodigo =	'001',
        pedpordesc =	0.000000,
        pedusudesc =	'',
        artaplipro =	0,
        pedvalinter =	0.000000,
        medcodigo =	'UNI',
        marcodigo =	'ISM',
        artpeso =	'0.00',
        artserie =	0,
        artservicio =	-1,
        artexpins =	0,
        audnumxml =	None,
        artfaccero =	0,
        integracodigo =	'000',
        proyectocodigo =	'000',
        pedfecposent =	hoy,
        pedcantfacturado =	0.000000,
        pedpordescori =	0.000000,
        pedprecioori =	10.000000,
        prosecuen =	1,
        jefecodigo =	'000',
        artdescri =	artdescri,
        pedusuaped =	None,
        pedfecaped =	None,
        pedhoraped =	None,
        pedestaped =	None,
        pedusuapro =	None,
        pedfecapro =	None,
        pedhorapro =	None,
        pedestapro =	None,
        # campoExtra =	None,
        # campoExtra =	None,
        # campoExtra =	None,
        # campoExtra =	None,
        # campoExtra =	mesacodigo,
        # campoExtra =	0,
        # campoExtra =	None,
        # campoExtra =	@pedcomencoci,
    )
    try:
        db.session.add(_nuevoDetalle)
        db.session.commit()
        return {'mensaje': 'detalle creado exitosamente'}
    except Exception as e:
        print(e)
        return {'error': str(e)}, 500
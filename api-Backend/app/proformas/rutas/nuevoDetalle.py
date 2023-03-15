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
#   "pedsecuen": "pedsecuen", # TODO: va incrementadndo con un query
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

    # TODO: preguntar aqui por la multiplcacion LA MULTIPLICACION es por sysiva/100
    # (select (artprecventa1*0.12) * @pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    artprecventa1_12 = inmart.query.filter_by(artcodigo=data['artcodigo']).first().artprecventa1 # TODO: hacer la multiplicacion

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
        #TODO aqui esta el tipcodigo ademas de otros campos
        # select  * from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001' and ciacodigo ='01'

        ciacodigo =	@ciacodigo,
        pednumped =	@pednumped,
        pedsecuen =	@pedsecuen,
        facnumfac =	NULL,
        pedtipo =	'PR' ,
        pedapliiva =	-1, #TODO: viene de inmart campo artapliiva
        factippag =	'EFE', #ta bien, viene de cxcbformapag
        moncodigo =	'D',
        pedcambio =	0.00,
        pedfecemi =	${fechaSistema},
        clicodigo =	(select clicodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
        loccodigo =	@loccodigo,
        cliprecio =	1, # precio que maneja el cliente TODO2
        pedstatus =	@pedstatus,
        bodcodigo =	'', # inbbod es la tabla, es el codigo de la bodega, TODO: recivir en el json
        invcodigo =	'01',
        artcodigo =	@artcodigo,
        precodigo =	'01',#TODO: viene de inmart campo precodigo
        coscodigo =	'',
        lincodigo =	(select lincodigo from SiacIlsaboremio.dbo.inmart where artcodigo = @artcodigo),
        vencodigo =	(select vencodigo from SiacIlsaboremio.dbo.facped where pednumped = @pednumped),
        zoncodigo =	(select zoncodigo from SiacIlsaboremio.dbo.facped where pednumped = @pednumped),
        sercodigo =	'',
        pedcantidad =	@pedcantidad,
        pedcosto =	0.000000,
        pedcostodol =	0.000000,
        pedpreven =	(select artprecventa1 from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
        pedvaldesglo =	0.000000,
        pedvaldesc =	0.000000,
        pedvalrec =	0.000000,
        pediva =	12.00, #TODO esta en siacsys campo es sysiva

        # TODO: subir todos una posicion
        pedvaliva =	#
        pedvalor =	(select (artprecventa1*0.12) * @pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
        pedvaltot =	(select (artprecventa1* @pedcantidad) from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
        pedfecisys =	(select ((artprecventa1*0.12) + artprecventa1)*@pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
        pedhorisys =	${fechaSistema},
        pedusuisys =	CONVERT (time, ${horaSistema}),
        pedestisys =	@pedusuisys,
        pedfecmsys =	User, #TODO2 lo envia por post pero podria ser el nombre de la maquina o la ip
        pedhormsys =	${fechaSistema},
        pedusumsys =	CONVERT (time, ${horaSistema}),
        pedestmsys =	@pedusuisys, # es usuario modifica osea va en el update del delatte
        tipcodigo =	User,
        pedpordesc =	'001', #TODO: esta en cxcmcli campo tipcodigo mirar arriba en el query
        pedusudesc =	0.000000,
        artaplipro =	'',
        pedvalinter =	0, #TODO2 aplica promocion en el futuro
        medcodigo =	0.000000,
        marcodigo =	'UNI', #TODO: viene de inmart campo medcodigo
        artpeso =	'ISM',#TODO: viene de inmart campo marcodigo
        artserie =	'0.00',#TODO: viene de inmart campo artpeso
        artservicio =	0,#TODO: viene de inmart campo artserie
        artexpins =	-1,#TODO: viene de inmart campo artservicio
        audnumxml =	0,#TODO: viene de inmart campo artexpins
        artfaccero =	NULL,
        integracodigo =	0,#TODO: viene de inmart campo artfaccero
        proyectocodigo =	'000',
        pedfecposent =	'000',
        pedcantfacturado =	${fechaSistema},
        pedpordescori =	0.000000, # como es nuevodetalle va cero, para actualizar se ha de poner datos
        pedprecioori =	0.000000,# como es nuevodetalle va cero, para actualizar se ha de poner datos
        prosecuen =	0.000000,
        jefecodigo =	1, #TODO: vamo a ver maniana en la auditoria XD
        artdescri =	'000',
        pedusuaped =	(select artdescri from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
        pedfecaped =	NULL,
        pedhoraped =	NULL,
        pedestaped =	NULL,
        pedusuapro =	NULL,
        pedfecapro =	NULL,
        pedhorapro =	NULL,
        pedestapro =	NULL,
    
    )
    try:
        db.session.add(_nuevoDetalle)
        db.session.commit()
        return {'mensaje': 'detalle creado exitosamente'}
    except Exception as e:
        print(e)
        return {'error': str(e)}, 500
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
#   "user": "user",
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
    # (select vencodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
    # (select zoncodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
    # (select mesacodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
    query_cabecera = db.session.query(
        Cabecera.clicodigo,
        Cabecera.vencodigo,
        Cabecera.zoncodigo,
        # Cabecera.mesacodigo,
    ).filter(Cabecera.pednumped == data['pednumped']
    ).first()

    clicodigo = query_cabecera.clicodigo
    vencodigo = query_cabecera.vencodigo
    zoncodigo = query_cabecera.zoncodigo


    # (select lincodigo from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    # (select artprecventa1 from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    # (select (artprecventa1*0.12) * @pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    # (select (artprecventa1* @pedcantidad) from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    # (select ((artprecventa1*0.12) + artprecventa1)*@pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    # (select artdescri from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
    query_inmart = db.session.query(
        inmart.lincodigo,
        inmart.artprecventa1,
        inmart.artdescri,
    ).filter(Cabecera.artcodigo == data['artcodigo']
    ).first()

    lincodigo = query_inmart.lincodigo

    # TODO: preguntar aqui por la multiplcacion LA MULTIPLICACION es por sysiva/100
    artprecventa1 = query_inmart.artprecventa1
    artprecventa1_12 = query_inmart.artprecventa1 * 0.12
    artprecventa1_pedcantidad = query_inmart.artprecventa1 * data['pedcantidad']
    artprecventa1_12_pedcantidad = (query_inmart.artprecventa1 * 0.12) + query_inmart.artprecventa1 * data['pedcantidad']
   
    artdescri = query_inmart.artdescri




    hoy = datetime.now().strftime("%Y-%m-%d 00:00:00.%f")[:-3]
    hoy_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    _nuevoDetalle = Detalle(
        #TODO aqui esta el tipcodigo ademas de otros campos
        # select  * from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001' and ciacodigo ='01'
        ciacodigo =	data['ciacodigo'],
        pednumped =	data['pednumped'],
        pedsecuen =	data['pedsecuen'],
        facnumfac =	None,
        pedtipo =	'PR' ,
        pedapliiva =	-1, #TODO: viene de inmart campo artapliiva
        factippag =	'EFE', #ta bien, viene de cxcbformapag
        moncodigo =	'D',
        pedcambio =	0.00,
        pedfecemi =	hoy,
        clicodigo =	clicodigo,
        loccodigo =	data['loccodigo'],
        cliprecio =	1, # precio que maneja el cliente TODO2
        pedstatus =	data['pedstatus'],
        bodcodigo =	'', # inbbod es la tabla, es el codigo de la bodega, TODO: recivir en el json
        invcodigo =	'01',
        artcodigo =	data['artcodigo'],
        precodigo =	'01',#TODO: viene de inmart campo precodigo
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
        pediva =	12.00, #TODO esta en siacsys campo es sysiva
        pedvaliva =	artprecventa1_12,
        pedvalor =	artprecventa1_pedcantidad,
        pedvaltot =	artprecventa1_12_pedcantidad,
        pedfecisys =	hoy,
        pedhorisys =	hoy_hora,
        pedusuisys =	data['pedusuisys'],
        pedestisys =	data['user'], #TODO2 lo envia por post pero podria ser el nombre de la maquina o la ip
        pedfecmsys =	hoy,
        pedhormsys =	hoy_hora,
        pedusumsys =	data['pedusuisys'], # es usuario modifica osea va en el update del delatte
        pedestmsys =	data['user'],
        tipcodigo =	'001', #TODO: esta en cxcmcli campo tipcodigo mirar arriba en el query
        pedpordesc =	0.000000,
        pedusudesc =	'',
        artaplipro =	0, #TODO2 aplica promocion en el futuro
        pedvalinter =	0.000000,
        medcodigo =	'UNI', #TODO: viene de inmart campo medcodigo
        marcodigo =	'ISM',#TODO: viene de inmart campo marcodigo
        artpeso =	'0.00',#TODO: viene de inmart campo artpeso
        artserie =	0,#TODO: viene de inmart campo artserie
        artservicio =	-1,#TODO: viene de inmart campo artservicio
        artexpins =	0,#TODO: viene de inmart campo artexpins
        audnumxml =	None,
        artfaccero =	0,#TODO: viene de inmart campo artfaccero
        integracodigo =	'000',
        proyectocodigo =	'000',
        pedfecposent =	hoy,
        pedcantfacturado =	0.000000, # como es nuevodetalle va cero, para actualizar se ha de poner datos
        pedpordescori =	0.000000,# como es nuevodetalle va cero, para actualizar se ha de poner datos
        pedprecioori =	0.000000,
        prosecuen =	1, #TODO: vamo a ver maniana en la auditoria XD
        jefecodigo =	'000',
        artdescri =	artdescri,
        pedusuaped =	None,
        pedfecaped =	None,
        pedhoraped =	None,
        pedestaped =	None,
        pedusuapro =	None,
        pedfecapro =	None,
        pedhorapro =	None,
        pedestapro = None
    )


    try:
        db.session.add(_nuevoDetalle)
        db.session.commit()
        return {'mensaje': 'detalle creado exitosamente'}
    except Exception as e:
        print(e)
        return {'error': str(e)}, 500
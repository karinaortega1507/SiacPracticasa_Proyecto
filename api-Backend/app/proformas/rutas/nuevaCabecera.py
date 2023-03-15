from datetime import datetime
import json
from flask import jsonify, request
from app.proformas import bp
from app.extensions import db
from flask_cors import cross_origin
from app.models.Cabecera import Cabecera, CabeceraSchema
from app.models.Detalle import Detalle, DetalleSchema
from app.models.fapvendedor import Fapvendedor, FapvendedorSchema
from app.models.cxcmcli import Cxcmcli, CxcmcliSchema
from app.models.SiacSys import SiacSys, SiacSysSchema

# recive esta estructura
# {
#   "user": "user",
#   "numped": "numped",
#   "pedtivapor": "pedtivapor",
#   "pedsubtot": "pedsubtot",
#   "pediva": "pediva",
#   "pedtotal": "pedtotal",
#   "pedusuisys": "pedusuisys",
#   "ciacodigo": "ciacodigo",
#   "loccodigo": "loccodigo",
#   "pedvalser": "pedvalser",
#   "mesacodigo": "mesacodigo",
# }
@bp.route('/nuevaCabecera', methods=['POST'])
@cross_origin()
def nuevaCabecera():
    data = request.json

    # vencodigo = (select vencodigo from SiacPracticasa.dbo.fapvendedor where 1=1 and usrcodigo=data['pedusuisys'] and ciacodigo = data['ciacodigo'] and loccodigo=data['loccodigo'])
    vencodigo = db.session.query(Fapvendedor.vencodigo).filter(
        Fapvendedor.usrcodigo == data['pedusuisys'],
        Fapvendedor.ciacodigo == data['ciacodigo'],
        Fapvendedor.loccodigo == data['loccodigo']
    ).first()

    vencodigo_result = FapvendedorSchema().dump(vencodigo)

    # zoncodigo = (select zoncodigo from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001')
    # tipcodigo = (select tipcodigo from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001')
    # regcodigo = (select regcodigo from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001'),
    # ciucodigo = (select ciucodigo from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001'),
    # procodigo = (select procodigo from SiacPracticasa.dbo.cxcmcli where clicodigo ='000001'),
    codigos = db.session.query(
        Cxcmcli.zoncodigo,
        Cxcmcli.tipcodigo,
        Cxcmcli.regcodigo,
        Cxcmcli.ciucodigo,
        Cxcmcli.procodigo
    ).filter(Cxcmcli.clicodigo == '000001',
             Cxcmcli.ciacodigo == data['ciacodigo']
    ).first()
    ## TODO: no es el first es por ciacodigo
    ## DONE: ya lo arregle

    # Serialize the result using Marshmallow schema
    cxcmcli_schema = CxcmcliSchema()
    codigos_result = cxcmcli_schema.dump(codigos)

    # top = (select top 1 sysservicio from SiacPracticasa.dbo.SiacSys)
    # top = db.session.query(SiacSys.sysservicio).limit(1).first()

    # siacsys_schema = SiacSysSchema()
    # top_result = siacsys_schema.dump(top)
    top_result = None
    
    hoy = datetime.now().strftime("%Y-%m-%d 00:00:00.%f")[:-3]
    hoy_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
    _nuevaCabecera = Cabecera(
        ciacodigo =	'01',
        pednumped =	data['numped'],
        loccodigo =	'01',
        facnumfac =	None,
        pedtipo   =	'PR',
        factippag =	'EFE',
        moncodigo =	'D',
        clicodigo =	'000001',
        garcodigo =	'000001',
        peddirent =	'GUAYAQUIL',
        pedcambio =	0.00,
        pedfecemi =	hoy,#.strftime('%Y-%m-%d %H:%M:%S.%f'),
        pedfecven =	hoy,#.strftime('%Y-%m-%d %H:%M:%S.%f'),
        pedtivacer =	0.00,
        pedtivapor =	data['pedtivapor'],
        pedsubtot =	data['pedsubtot'],
        pediva =	data['pediva'],
        pedtotal =	data['pedtotal'],
        pedstatus =	'P',
        peddetalle =	'prueba app mobile',
        pedfecisys =	hoy,#.strftime('%Y-%m-%d %H:%M:%S.%f'),
        pedhorisys =	hoy_hora,#.strftime('%Y-%m-%d %H:%M:%S.%f'),
        pedusuisys =	data['pedusuisys'],
        pedestisys =	data['user'],
        pedfecmsys =	hoy,#.strftime('%Y-%m-%d %H:%M:%S.%f'),
        pedhormsys =	hoy_hora,#.strftime('%Y-%m-%d %H:%M:%S.%f'),
        pedusumsys =	data['pedusuisys'],
        pedestmsys =	data['user'],
        pedusudes =	None,
        vencodigo =	vencodigo_result['vencodigo'],#data['pedusuisys'],
        zoncodigo =	codigos_result['zoncodigo'],
        pedpordes =	0.00,
        peddesglobal =	0.00,
        peddesdirecto =	0.00,
        pedrecargo =	0.00,
        tipcodigo =	codigos_result['tipcodigo'],
        pedporrec =	0.00,
        pedporiva =	12.00,
        pedvalantici =	0.00,
        forintmen =	0.00,
        pedvalinter =	0.00,
        fordias =	0,
        fortipo =	'CC',
        forcuotas =	1,
        foraplianti =	0,
        foranticipo =	0.00,
        foraplirango =	0,
        formondesde =	0.00,
        formonhasta =	0.00,
        forapligrac =	0,
        fordiasgrac =	0,
        forcuoinigr =	0,
        pedusuanti =	None,
        codcodigo =	None,
        adinumero =	None,
        pednumadi =	0,
        pedvaladi =	0.00,
        pedapliiva =	-1,
        pedconser =	0,
        pedlockser =	None,
        pedvehi =	0,
        audnumxml =	None,
        integracodigo =	'000',
        proyectocodigo =	'000',
        foraprocredito =	0,
        foraprologistica =	0,
        foraprocliente =	0,
        pedaprocredito =	0,
        pedaprologistica =	0,
        pedaprocliente =	0,
        pedproyecto =	0,
        pedsolsinstock =	0,
        pedsinstock =	0,
        forpromocion =	0,
        fordescuento =	0.00,
        regcodigo =	codigos_result['regcodigo'],
        ciucodigo =	codigos_result['ciucodigo'],
        procodigo =	codigos_result['procodigo'],
        pedcierre =	0,
        prosecuen =	1,
        pedusuaped =	None,
        pedfecaped =	hoy,
        pedhoraped =	hoy,
        pedestaped =	None,
        pedusuapro =	None,
        pedfecapro =	hoy,
        pedhorapro =	hoy,
        pedestapro =	None,
        pedvallincre =	0.00,
        contelef =	None,
        transcodigo =	'000',
        pedforent =	'B',
        pedcedentrega =	None,
        pednomentrega =	None,
        nomcontacto =	None,
        pedwip =	' ',
        peddetalle1 =	top_result,
        peddetalle2 =	data['pedvalser'],
        peddetalle3 =	data['mesacodigo']
    )


    # cabecera_schema = CabeceraSchema()
    # cabecera = cabecera_schema.load(_nuevaCabecera,session=db.session)
    try:
        db.session.add(_nuevaCabecera)
        db.session.commit()
        return {'mensaje': 'cabecera creada exitosamente'}
    
    except Exception as e:
        print(e)
        return {'error': str(e)}, 500
    

    
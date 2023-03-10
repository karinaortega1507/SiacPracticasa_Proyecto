# from datetime import datetime
# import json
# from flask import jsonify, request
# from app.models.Cabecera import Cabecera
# from app.models.Detalle import Detalle
# from app.models.inmart import inmart
# from app.proformas import bp
# from app.extensions import db
# from flask_cors import cross_origin


# # recive esta estructura:
# # {
# #   "ciacodigo": "ciacodigo",
# #   "pednumped": "pednumped",
# #   "pedsecuen": "pedsecuen",
# #   "facnumfac": "facnumfac",
# #   "pedtipo": "pedtipo",
# #   "pedapliiva": "pedapliiva",
# #   "factippag": "factippag",
# #   "moncodigo": "moncodigo",
# # }
# @bp.route('/nuevoDetalle', methods=['POST'])
# @cross_origin()
# def nuevoDetalle():
#     # (select clicodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
#     clicodigo = Cabecera.query.filter_by(pednumped=request.form['pednumped']).first()

#     # (select lincodigo from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
#     lincodigo = inmart.query.filter_by(artcodigo=request.form['artcodigo']).first()

#     # (select vencodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
#     vencodigo = Cabecera.query.filter_by(pednumped=request.form['pednumped']).first()

#     # (select zoncodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
#     zoncodigo = Cabecera.query.filter_by(pednumped=request.form['pednumped']).first()

#     # (select artprecventa1 from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
#     artprecventa1 = inmart.query.filter_by(artcodigo=request.form['artcodigo']).first()

#     # TODO: preguntar aqui por la multiplcacion
#     # (select (artprecventa1*0.12) * @pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
#     artprecventa1_12 = inmart.query.filter_by(artcodigo=request.form['artcodigo']).first()

#     # (select (artprecventa1* @pedcantidad) from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
#     artprecventa1_pedcantidad = inmart.query.filter_by(artcodigo=request.form['artcodigo']).first()

#     # (select ((artprecventa1*0.12) + artprecventa1)*@pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
#     artprecventa1_12_pedcantidad = inmart.query.filter_by(artcodigo=request.form['artcodigo']).first()

#     # (select artdescri from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
#     artdescri = inmart.query.filter_by(artcodigo=request.form['artcodigo']).first()

#     # (select mesacodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
#     mesacodigo = Cabecera.query.filter_by(pednumped=request.form['pednumped']).first()


#     detalle = Detalle(
#         # ciacodigo=request.form['ciacodigo'],
#         # pednumped=request.form['pednumped'],
#         # pedsecuen=request.form['pedsecuen'],
#         # facnumfac=None,
#         # pedtipo='PR',
#         # factippag='-1',
#         # moncodigo='EFE',
#         # Aquí se colocarían todas las columnas correspondientes a la tabla "fatped"

#         ciacodigo       =  request.form['ciacodigo'],
#         pednumped       =  request.form['pednumped'],
#         pedsecuen       =  request.form['pedsecuen'],
#         loccodigo       =   
#         facnumfac       =   
#         pedtipo         =   
#         pedapliiva      =   
#         factippag       =   
#         moncodigo       =   
#         pedcambio       =   
#         pedfecemi       =   
#         clicodigo       =   
#         cliprecio       =   
#         pedstatus       =   
#         bodcodigo       =   
#         invcodigo       =   
#         artcodigo       =   
#         precodigo       =   
#         coscodigo       =   
#         lincodigo       =   
#         vencodigo       =   
#         zoncodigo       =   
#         sercodigo       =   
#         pedcantidad     =   
#         pedcosto        =   
#         pedcostodol     =   
#         pedpreven       =   
#         pedvaldesglo    =   
#         pedvaldesc      =   
#         pedvalrec       =   
#         pediva          =   
#         pedvaliva       =   
#         pedvalor        =   
#         pedvaltot       =   
#         pedfecisys      =   
#         pedhorisys      =   
#         pedusuisys      =   
#         pedestisys      =   
#         pedfecmsys      =   
#         pedhormsys      =   
#         pedusumsys      =   
#         pedestmsys      =   
#         tipcodigo       =   
#         pedpordesc      =   
#         pedusudesc      =   
#         artaplipro      =   
#         pedvalinter     =   
#         medcodigo       =   
#         marcodigo       =   
#         artpeso         =   
#         artserie        =   
#         artservicio     =   
#         artexpins       =   
#         audnumxml       =   
#         artfaccero      =   
#         integracodigo   =   
#         proyectocodigo  =   
#         pedfecposent    =   
#         pedcantfacturado=   
#         pedpordescori   =   
#         pedprecioori    =   
#         prosecuen       =   
#         jefecodigo      =   
#         artdescri       =   
#         pedusuaped      =   
#         pedfecaped      =   
#         pedhoraped      =   
#         pedestaped      =   
#         pedusuapro      =   
#         pedfecapro      =   
#         pedhorapro      =   
#         pedestapro      =   
#         #71

# @ciacodigo,
# @pednumped,
# @pedsecuen,
# NULL,
# 'PR',
# -1,
#  'EFE',
# 'D',
# 0.00,
# ${fechaSistema},
# (select clicodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
# @loccodigo,
# 1,
# @pedstatus,
# '',
# '01',
# @artcodigo,
# '01',
# '',
# (select lincodigo from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
# (select vencodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
# (select zoncodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
# '',
# @pedcantidad,
# 0.000000,
#  0.000000,
# (select artprecventa1 from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
# 0.000000,
# 0.000000,
#  0.000000,
#  12.00,
# (select (artprecventa1*0.12) * @pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
# (select (artprecventa1* @pedcantidad) from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
# (select ((artprecventa1*0.12) + artprecventa1)*@pedcantidad from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
# ${fechaSistema},
# CONVERT (time,${horaSistema}),
# @pedusuisys,
# User,
# ${fechaSistema},
# CONVERT (time,${horaSistema}),
# @pedusuisys,
# User,
# '001',
# 0.000000,
# '',
# 0,
# 0.000000,
# 'UNI',
# 'ISM',
# '0.00',
# 0,
# -1,
#  0,
# NULL,
#  0,
# '000',
# '000',
# ${fechaSistema},
#  0.000000,
#  0.000000,
# 10.000000,
# 1,
# '000',
#  (select artdescri from SiacIlsaboremio.dbo.inmart where artcodigo=@artcodigo),
# NULL,
# NULL,
# NULL,
# NULL,
# NULL,
# NULL,
# NULL,
# NULL,
#  NULL,
#  NULL,
#  NULL,
#  NULL,
#  (select mesacodigo from SiacIlsaboremio.dbo.facped where pednumped =@pednumped),
#  0,
#  NULL,
#  @pedcomencoci,
# #79

#     )

#     db.session.add(detalle)
#     db.session.commit()

#     return 'Registro insertado correctamente', 201
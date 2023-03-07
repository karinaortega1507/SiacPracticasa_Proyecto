from urllib import request
from flask import jsonify
from flask_cors import cross_origin
from app.productos import bp
from app.extensions import db
from app.models.producto import Producto
from app.models.medida import Medida
from app.models.marca import Marca
from app.models.presentacion import Presentacion
from app.models.linea import Linea

@bp.route('/obtener_productos', methods=['GET'])
@cross_origin()
def obtener_productos():
    query_result = db.session.query(
        Producto.artcodigo.label('codigo'),
        Producto.artdescri.label('descripcion'),
        Producto.artprecventa1.label('precio'),
        Medida.meddescri.label('medida'),
        Marca.mardescri.label('marca'),
        Presentacion.predescri.label('presentacion'),
        Linea.lindescri.label('linea'),
        Producto.tmpcantidadimpresion.label('cantidad_etiquetas'),
   ).join(Marca, Producto.marcodigo == Marca.marcodigo)\
    .join(Medida, Producto.medcodigo == Medida.medcodigo)\
    .join(Presentacion, Producto.precodigo == Presentacion.precodigo)\
    .join(Linea, Producto.lincodigo == Linea.lincodigo)\
    .filter(
        Producto.ciacodigo == '01' and
        Producto.artprodven != 0 #and
        #Producto.artcodigo == '00018'
    ).order_by(Producto.artcodigo).all()

    # El resultado de la consulta es un objeto Row, que no puede ser serializado en JSON directamente.
    # Para convertir los objetos Row en diccionarios se utiliza el método as_dict() que se puede agregar en el modelo de SQLAlchemy. 
    # Luego, se puede construir una lista de diccionarios y devolverla como una respuesta JSON
    data = [row._asdict() for row in query_result]
    
    return jsonify(data)

@bp.route('/obtener_productos/<codigo_Prod>', methods=['GET'])
@cross_origin()
def obtener_productos_por_codigo(codigo_Prod):
    print(codigo_Prod)
    
    query_result = db.session.query(
    Producto.artcodigo.label('codigo'),
    Producto.artdescri.label('descripcion'),
    Producto.artprecventa1.label('precio'),
    Medida.meddescri.label('medida'),
    Marca.mardescri.label('marca'),
    Presentacion.predescri.label('presentacion'),
    Linea.lindescri.label('linea'),
    Producto.tmpcantidadimpresion.label('cantidad_etiquetas'),
).join(Marca, Producto.marcodigo == Marca.marcodigo)\
.join(Medida, Producto.medcodigo == Medida.medcodigo)\
.join(Presentacion, Producto.precodigo == Presentacion.precodigo)\
.join(Linea, Producto.lincodigo == Linea.lincodigo)\
.filter(
    
    Producto.artcodigo == str(codigo_Prod)
).order_by(Producto.artcodigo).all()

# El resultado de la consulta es un objeto Row, que no puede ser serializado en JSON directamente.
# Para convertir los objetos Row en diccionarios se utiliza el método as_dict() que se puede agregar en el modelo de SQLAlchemy. 
# Luego, se puede construir una lista de diccionarios y devolverla como una respuesta JSON
    data = [row._asdict() for row in query_result]
    
    return jsonify(data)

    


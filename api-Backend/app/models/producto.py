from app.extensions import db, PrimaryKeyConstraint
from app.extensions import ma

class Producto(db.Model):
    __tablename__ = 'inmart'
    __table_args__ = {'schema': 'SiacPracticasa.dbo'}

    artcodigo = db.Column(db.String(15))
    ciacodigo = db.Column(db.String(2))
    invcodigo = db.Column(db.String(2))
    artprodven =  db.column(db.Integer)
    precodigo = db.Column(db.String(2))
    artdescri = db.Column(db.String(200))
    artprecventa1 = db.Column (db.Numeric(precision=18, scale=8))
    marcodigo = db.Column(db.String(5))
    medcodigo = db.Column(db.String(3))
    lincodigo = db.Column(db.String(20))
     # campo temporal del modelo Producto para la cantidad de etiquetas a imprimir
    tmpcantidadimpresion = db.Column(db.Integer)

    __table_args__ = (
      PrimaryKeyConstraint('ciacodigo', 'invcodigo', 'artcodigo', name='pk_inmart'),
        {'schema': 'SiacPracticasa.dbo'}
    )
    
class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: Producto


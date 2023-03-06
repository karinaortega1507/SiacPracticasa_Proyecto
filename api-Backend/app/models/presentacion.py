from app.extensions import db, PrimaryKeyConstraint
from app.extensions import ma

class Presentacion(db.Model):
    __tablename__ = 'inbpre'
    __table_args__ = {'schema': 'SiacPracticasa.dbo'}

    ciacodigo = db.Column(db.String(2))
    precodigo = db.Column(db.String(2))
    predescri = db.Column(db.String(30))

    __table_args__ = (
      PrimaryKeyConstraint('ciacodigo', 'precodigo', name='pk_inbpre'),
        {'schema': 'SiacPracticasa.dbo'}
    )
   
class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: Presentacion
    
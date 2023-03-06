from app.extensions import db, PrimaryKeyConstraint
from app.extensions import ma

class Linea(db.Model):
    __tablename__ = 'inblin'
    __table_args__ = {'schema': 'SiacPracticasa.dbo'}

    ciacodigo = db.Column(db.String(2))
    lincodigo = db.Column(db.String(20))
    lindescri = db.Column(db.String(40))

    __table_args__ = (
      PrimaryKeyConstraint('ciacodigo', 'lincodigo', name='pk_inblin'),
        {'schema': 'SiacPracticasa.dbo'}
    )
    
class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: Linea
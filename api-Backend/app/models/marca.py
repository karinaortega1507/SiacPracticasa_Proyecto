from app.extensions import db, PrimaryKeyConstraint
from app.extensions import ma

class Marca(db.Model):
    __tablename__ = 'inbmar'
    __table_args__ = {'schema': 'SiacPracticasa.dbo'}

    ciacodigo = db.Column(db.String(2))
    marcodigo = db.Column(db.String(5))
    mardescri = db.Column(db.String(30))

    __table_args__ = (
      PrimaryKeyConstraint('ciacodigo', 'marcodigo', name='pk_inbmar'),
        {'schema': 'SiacPracticasa.dbo'}
    )
   
class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: Marca
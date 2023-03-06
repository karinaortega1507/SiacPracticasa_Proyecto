from app.extensions import db, PrimaryKeyConstraint
from app.extensions import ma

class Medida(db.Model):
    __tablename__ = 'inbmed'
    __table_args__ = {'schema': 'SiacPracticasa.dbo'}

    ciacodigo = db.Column(db.String(2))
    medcodigo = db.Column(db.String(3))
    meddescri = db.Column(db.String(30))

    __table_args__ = (
      PrimaryKeyConstraint('ciacodigo', 'medcodigo', name='pk_inbmed'),
        {'schema': 'SiacPracticasa.dbo'}
    )
   
class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: Medida
from app.extensions import db
from app.extensions import ma

class siacPracticasaSiacusr(db.Model):
    __tablename__ = 'siaccusr'
    __table_args__ = {'schema': 'SiacPracticasa.dbo'}
    id = db.column(db.Integer)
    usrclave = db.column(db.String(10))
    usrcodigo = db.column(db.String(10), primary_key=True)
    usrcodper = db.column(db.String(10))
    usrcorreo = db.column(db.String(60))
    usrdiascaduclave = db.column(db.Integer)
    usremail = db.column(db.String(60))
    usrestisys = db.column(db.String(40))
    usrestmsys = db.column(db.String(40))
    usrfecactuclave = db.column(db.DateTime)
    usrfeccad = db.column(db.DateTime)
    usrfecisys = db.column(db.DateTime)
    usrfecmsys = db.column(db.DateTime)
    usrflagnuevmodi = db.column(db.Integer)
    usrflagoficre = db.column(db.Integer)
    usrflagperfil = db.column(db.Integer)
    usrflagupdateperfilacces = db.column(db.Boolean)
    usrhelpart = db.column(db.String(1))
    usrhelpcli = db.column(db.String(1))
    usrhelppro = db.column(db.String(1))
    usrhorisys = db.column(db.DateTime)
    usrhormsys = db.column(db.DateTime)
    usrimagen = db.column(db.LargeBinary)
    usrimagentype = db.column(db.String(50))
    usrnombre = db.column(db.String(60))
    usrpassword = db.column(db.String(50))
    usrstatus = db.column(db.String(1))
    usrusuisys = db.column(db.String(10))
    usrusumsys = db.column(db.String(10))




    def __init__(self, id, usrclave, usrcodigo, usrcodper, usrcorreo, usrdiascaduclave, usremail, usrestisys, usrestmsys, usrfecactuclave, usrfeccad, usrfecisys, usrfecmsys, usrflagnuevmodi, usrflagoficre, usrflagperfil, usrflagupdateperfilacces, usrhelpart, usrhelpcli, usrhelppro, usrhorisys, usrhormsys, usrimagen, usrimagentype, usrnombre, usrpassword, usrstatus, usrusuisys, usrusumsys):
        self.id = id
        self.usrclave = usrclave
        self.usrcodigo = usrcodigo
        self.usrcodper = usrcodper
        self.usrcorreo = usrcorreo
        self.usrdiascaduclave = usrdiascaduclave
        self.usremail = usremail
        self.usrestisys = usrestisys
        self.usrestmsys = usrestmsys
        self.usrfecactuclave = usrfecactuclave
        self.usrfeccad = usrfeccad
        self.usrfecisys = usrfecisys
        self.usrfecmsys = usrfecmsys
        self.usrflagnuevmodi = usrflagnuevmodi
        self.usrflagoficre = usrflagoficre
        self.usrflagperfil = usrflagperfil
        self.usrflagupdateperfilacces = usrflagupdateperfilacces
        self.usrhelpart = usrhelpart
        self.usrhelpcli = usrhelpcli
        self.usrhelppro = usrhelppro
        self.usrhorisys = usrhorisys
        self.usrhormsys = usrhormsys
        self.usrimagen = usrimagen
        self.usrimagentype = usrimagentype
        self.usrnombre = usrnombre
        self.usrpassword = usrpassword
        self.usrstatus = usrstatus
        self.usrusuisys = usrusuisys
        self.usrusumsys = usrusumsys


class siacPracticasaSiacusrSchema(ma.Schema):
    class Meta:
        fields = (
                'id', 'usrclave', 'usrcodigo', 'usrcodper', 'usrcorreo',
                'usrdiascaduclave', 'usremail', 'usrestisys', 'usrestmsys',
                'usrfecactuclave', 'usrfeccad', 'usrfecisys', 'usrfecmsys',
                'usrflagnuevmodi', 'usrflagoficre', 'usrflagperfil',
                'usrflagupdateperfilacces', 'usrhelpart', 'usrhelpcli',
                'usrhelppro', 'usrhorisys', 'usrhormsys', 'usrimagen',
                'usrimagentype', 'usrnombre', 'usrpassword', 'usrstatus',
                'usrusuisys', 'usrusumsys'
            )

siacPracticasaSiacusr_schema = siacPracticasaSiacusrSchema()
siacPracticasaSiacusr_schema_varios = siacPracticasaSiacusrSchema(many=True)

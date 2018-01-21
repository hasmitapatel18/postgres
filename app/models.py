from app import db


class Rep_class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(100), nullable=False)

class Rep_family(db.Model):
    __tablename__ = 'families'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rep_class= db.ForeignKey=('classes.id')

class Translated_products(db.Model):
    __tablename__ = 'translated_product'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    rep_family= db.ForeignKey=('families.id')

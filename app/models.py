from app import db


class Rep_class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(100), nullable=False)
    rep_families=db.relationship('Rep_family', backref='classes', lazy=True)

class Rep_family(db.Model):
    __tablename__ = 'families'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rep_class_id= db.Column(db.Integer, db.ForeignKey('classes.id'))
    rep_class=db.relationship('Rep_class')
    reps=db.relationship('Rep', backref='families', lazy=True)

class Rep(db.Model):
    __tablename__ = 'reps'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rep_family_id= db.Column(db.Integer, db.ForeignKey('families.id'))
    rep_family=db.relationship('Rep_family')
    translated_products=db.relationship('Translated_products', backref='reps', lazy=True)

class Translated_products(db.Model):
    __tablename__ = 'translated_product'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    aa_seq = db.Column(db.String(100000))
    rep_id= db.Column(db.Integer, db.ForeignKey('reps.id'))
    rep_rep=db.relationship('Rep')

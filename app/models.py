from app import db
from sqlalchemy import Index


class Rep_class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, index=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rep_families=db.relationship('Rep_family', backref='classes', lazy=True)



class Rep_family(db.Model):
    __tablename__ = 'families'
    id = db.Column (db.Integer, index=True, primary_key=True)
    name = db.Column(db.String(100))
    rep_class_id= db.Column(db.Integer, db.ForeignKey('classes.id'))
    rep_class=db.relationship('Rep_class')
    reps=db.relationship('Rep', backref='families', lazy=True)



class Rep(db.Model):
    __tablename__ = 'reps'
    id = db.Column (db.Integer, index=True, primary_key=True)
    name = db.Column(db.String(100))
    rep_family_id= db.Column(db.Integer, db.ForeignKey('families.id'))
    rep_family=db.relationship('Rep_family')
    translated_products=db.relationship('Information', backref='reps', lazy=True)




class Information(db.Model):
    __tablename__ = 'information'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    sw_score=db.Column(db.Integer)
    mili_div=db.Column(db.Integer)
    mili_del=db.Column(db.Integer)
    mili_ins=db.Column(db.Integer)
    geno_name=db.Column(db.String(100))
    geno_start=db.Column(db.Integer)
    geno_end=db.Column(db.Integer)
    geno_left=db.Column(db.Integer)
    strand=db.Column(db.Text)
    rclass= db.Column(db.String(100))
    rfamily= db.Column(db.String(100))
    rep_start=db.Column(db.Integer)
    rep_end=db.Column(db.Integer)
    rep_left=db.Column(db.Integer)
    dna_seq=db.Column(db.Text)
    aa_seq = db.Column(db.Text)
    rep_id= db.Column(db.Integer, db.ForeignKey('reps.id'))
    rep_rep=db.relationship('Rep')

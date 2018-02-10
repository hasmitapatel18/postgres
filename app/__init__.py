from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint, render_template, request, escape

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=True)

from app.models import *

def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    from app import models

    return app

@app.route('/')
def homepage():
    return render_template('homepage.html', title="homepage")

@app.route('/classespg/')
def classespg():
    class_name = request.args.get('class_name')
    rep_class = Rep_class.query.all()


    return render_template('classespg.html',rep_class=rep_class)

@app.route('/familiespg/')
def familiespg():
    class_name = request.args.get('class_name')
    if class_name == None:
        rep_family = Rep_family.query.all()
    else:
        rep_family = Rep_family.query.join(Rep_class).filter(Rep_class.name == class_name)


    return render_template('familiespg.html',rep_family=rep_family)

@app.route('/informationpg/')
def informationpg():
    class_name = request.args.get('class_name')
    family_name= request.args.get('family_name')
    rep_name = request.args.get('rep_name')

    if rep_name == None and family_name == None and class_name == None:
        rep_info=Information.query.all()

    if rep_name != None and family_name == None and class_name == None:
        rep_info=Information.query.join(Rep_family,Rep_class)\
        .filter(Rep_family.name == family_name and Rep_class.name == class_name)


    if rep_name != None and family_name != None and class_name == None:
        rep_info=Information.query.join(Rep_class).filter(Rep_class.name == class_name)


    if rep_name != None and family_name != None and class_name != None:
        rep_info=Information.query.join(Rep,Rep_family,Rep_class)\
        .filter(Rep.name==rep_name and Rep_family.name == family_name and Rep_class.name == class_name)

    return render_template('informationpg.html', rep_info=rep_info, class_name=class_name, family_name=family_name, rep_name=rep_name)

@app.route('/namespg/')
def namespg():
    class_name = request.args.get('class_name')
    family_name= request.args.get('family_name')

    if family_name == None and class_name == None:
        rep_name = Rep.query.all()

    if class_name != None and family_name != None:
        rep_name = Rep.query.join(Rep_family,Rep_class)\
            .filter(Rep_class.name == class_name and Rep_family.name == family_name)


    return render_template('namespg.html',rep_name=rep_name)

@app.route('/querypg/')
def querypg():
    aaseqquery= request.args.get('aaseqquery')
    aaquery=Information.query.filter_by(aa_seq=aaseqquery).first()
    class_search= (aaquery.rep_rep.rep_family.rep_class)
    family_search= (aaquery.rep_rep.rep_family)
    name_search= (aaquery.rep_rep)

    return render_template('querypg.html', class_search=class_search, family_search=family_search, name_search=name_search)

@app.route('/searchingaa/')
def searchingaa():

    return render_template('searchingaa.html')

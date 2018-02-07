from flask import Blueprint, render_template, request

from . import informationpg

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@informationpg.route('/')
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

    return render_template('informationpg.html', rep_info=rep_info)

from flask import Blueprint, render_template, request

from . import namespg

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@namespg.route('/')
def namespg():
    class_name = request.args.get('class_name')
    family_name= request.args.get('family_name')

    if family_name == None and class_name == None:
        rep_name = Rep.query.all()

    if class_name != None and family_name != None:
        rep_name = Rep.query.join(Rep_family,Rep_class)\
            .filter(Rep_class.name == class_name and Rep_family.name == family_name)


    return render_template('namespg.html',rep_name=rep_name)

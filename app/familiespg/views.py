from flask import Blueprint, render_template, request

from . import familiespg

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@familiespg.route('/')
def familiespg():
    class_name = request.args.get('class_name')
    if class_name == None:
        rep_family = Rep_family.query.all()
    else:
        rep_family = Rep_family.query.join(Rep_class).filter(Rep_class.name == class_name)


    return render_template('familiespg.html',rep_family=rep_family)

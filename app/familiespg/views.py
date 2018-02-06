from flask import Blueprint, render_template, request

from . import familiespg

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@familiespg.route('/')
def familiespg():
    family_name = request.args.get('family_name')
    rep_family = Rep_family.query.all()
    return render_template('familiespg.html',rep_family=rep_family)

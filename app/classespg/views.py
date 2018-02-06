from flask import Blueprint, render_template, request

from . import classespg

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@classespg.route('/')
def classespg():
    class_name = request.args.get('class_name')
    rep_class = Rep_class.query.all()

    return render_template('classespg.html',rep_class=rep_class)

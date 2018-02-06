from flask import Blueprint, render_template, request

from . import namespg

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@namespg.route('/')
def namespg():
    retroelement_name = request.args.get('retroelement_name')
    rep_name = Rep.query.all()
    return render_template('namespg.html',rep_name=rep_name)

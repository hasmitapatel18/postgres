from flask import Blueprint, render_template, request

from . import searchingaa

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@searchingaa.route('/')
def searchingaa():
    class_name = request.args.get('class_name')
    rep_class = Rep_class.query.filter_by(name=class_name).first()
    rep_families = rep_class.rep_families
    return render_template('searchingaa.html',rep_families=rep_families)

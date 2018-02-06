from flask import Blueprint, render_template, request

from . import informationpg

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@informationpg.route('/')
def informationpg():



    return render_template('informationpg.html', title="information")

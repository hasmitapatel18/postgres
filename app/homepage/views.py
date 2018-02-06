from flask import Blueprint, render_template

from . import homepage

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@homepage.route('/')
def homepage():



    return render_template('homepage.html', title="homepage")

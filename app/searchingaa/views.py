from flask import Blueprint, render_template, request

from . import searchingaa

from app import db

from app.models import Rep_class
from app.models import Rep_family
from app.models import Rep
from app.models import Information




@searchingaa.route('/')
def searchingaa():
    
    return render_template('searchingaa.html')

from flask import Blueprint

querypg = Blueprint('querypg', __name__)

from . import views

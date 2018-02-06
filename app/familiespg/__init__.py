from flask import Blueprint

familiespg = Blueprint('familiespg', __name__)

from . import views

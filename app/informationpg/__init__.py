from flask import Blueprint

informationpg = Blueprint('informationpg', __name__)

from . import views

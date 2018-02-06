from flask import Blueprint

classespg = Blueprint('classespg', __name__)

from . import views

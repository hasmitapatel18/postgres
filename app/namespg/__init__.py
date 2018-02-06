from flask import Blueprint

namespg = Blueprint('namespg', __name__)

from . import views

from flask import Blueprint

window = Blueprint('window', __name__)

from . import errors,  views
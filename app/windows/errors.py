from . import window
from flask import render_template

@window.errorhandler(404)
def page_not_found():
    return render_template('error/404.html')

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FileField, SubmitField
from werkzeug.serving import generate_adhoc_ssl_context
from wtforms.validators import Length, DataRequired


class AdminForm(FlaskForm):
    __slots__ = ''
    post_name = StringField('What is your name?')
    loc = StringField("Location")
    date = StringField("Date")
    link = StringField("LInk")
    file = FileField("Word of PDF required")

    @classmethod
    def shownow(cls):
        pass
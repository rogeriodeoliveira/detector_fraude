from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class TextSubmit(FlaskForm):
    texto = StringField("texto", widget=TextArea(),validators=[DataRequired()])
    link = StringField("link")
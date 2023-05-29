# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    book_title = StringField('Tytuł książki', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    submit = SubmitField('Dodaj książkę')
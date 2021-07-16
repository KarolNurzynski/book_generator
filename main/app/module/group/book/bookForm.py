from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, IntegerField

class BookForm(FlaskForm):
    id = HiddenField()
    author = StringField('Author')
    title = StringField('Title')
    submit = SubmitField("Save")

from creator.models import User
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class CharacterForm(FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired()])
    ancestry = StringField('Ancestry', validators=[DataRequired()])
    char_class = StringField('Class', validators=[DataRequired()])
    submit = SubmitField('Submit')

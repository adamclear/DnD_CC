from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError

class NewCharacterForm(FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired()])
    strength = IntegerField('Strength', validators=[DataRequired()])
    dexterity = IntegerField('Dexterity', validators=[DataRequired()])
    constitution = IntegerField('Constitution', validators=[DataRequired()])
    intelligence = IntegerField('Intelligence', validators=[DataRequired()])
    wisdom = IntegerField('Wisdom', validators=[DataRequired()])
    charisma = IntegerField('Charisma', validators=[DataRequired()])
    ancestry = StringField('Ancestry', validators=[DataRequired()])
    heroic_class = StringField('Class', validators=[DataRequired()])
    weapon = StringField('Weapon', validators=[DataRequired()])
    armor = StringField('Armor', validators=[DataRequired()])
    submit = SubmitField('Submit')

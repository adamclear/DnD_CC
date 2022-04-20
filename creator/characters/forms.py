from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Optional

class NewCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    ancestry = SelectField('Ancestry', choices=[
        '-Please Choose-', 'Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn',
        'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling'
    ], validators=[DataRequired()])
    heroic_class = SelectField('Class', choices=[
        '-Please Choose-', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter',
        'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'
    ], validators=[DataRequired()])
    weapon = SelectField('Weapon', choices=[
        '-Please Choose-', 'Battleaxe', 'Club', 'Crossbow-Light', 'Dagger',
        'Flail', 'Glaive', 'Greataxe',  'Greatclub', 'Greatsword', 'Halberd',
        'Longbow', 'Longsword', 'Mace', 'Maul', 'Rapier', 'Quarterstaff',
        'Scimitar', 'Shortbow', 'Shortsword', 'Spear'
    ], validators=[DataRequired()])
    armor = SelectField('Armor', choices=[
        '-Please Choose', 'Padded-Armor', 'Leather-Armor', 'Studded-Leather-Armor',
        'Hide-Armor', 'Chain-Shirt', 'Scale-Mail', 'Breastplate',
        'Half-Plate-Armor', 'Ring-Mail', 'Chain-Mail', 'Splint-Armor', 'Plate-Armor'
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')

class AbilityScoreForm(FlaskForm):
    strength = IntegerField('Strength', validators=[DataRequired()])
    dexterity = IntegerField('Dexterity', validators=[DataRequired()])
    constitution = IntegerField('Constitution', validators=[DataRequired()])
    intelligence = IntegerField('Intelligence', validators=[DataRequired()])
    wisdom = IntegerField('Wisdom', validators=[DataRequired()])
    charisma = IntegerField('Charisma', validators=[DataRequired()])
    plustwo = SelectField('+2 to Which Ability Score?', choices=[
        '-Please Choose-', 'Strength', 'Dexterity', 'Constitution',
         'Intelligence', 'Wisdom', 'Charisma'
         ])
    plusone = SelectField('+1 to Which Ability Score?', choices=[
        '-Please Choose-', 'Strength', 'Dexterity', 'Constitution',
         'Intelligence', 'Wisdom', 'Charisma'
         ])
    submit = SubmitField('Submit')

class AbilityScoreFormHuman(FlaskForm):
    strength = IntegerField('Strength', validators=[DataRequired()])
    dexterity = IntegerField('Dexterity', validators=[DataRequired()])
    constitution = IntegerField('Constitution', validators=[DataRequired()])
    intelligence = IntegerField('Intelligence', validators=[DataRequired()])
    wisdom = IntegerField('Wisdom', validators=[DataRequired()])
    charisma = IntegerField('Charisma', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    weapon = SelectField('Weapon', choices=[
        '-Please Choose-', 'Battleaxe', 'Club', 'Crossbow-Light', 'Dagger',
        'Flail', 'Glaive', 'Greataxe',  'Greatclub', 'Greatsword', 'Halberd',
        'Longbow', 'Longsword', 'Mace', 'Maul', 'Rapier', 'Quarterstaff',
        'Scimitar', 'Shortbow', 'Shortsword', 'Spear'
    ], validators=[DataRequired()])
    armor = SelectField('Armor', choices=[
        '-Please Choose-', 'Padded-Armor', 'Leather-Armor', 'Studded-Leather-Armor',
        'Hide-Armor', 'Chain-Shirt', 'Scale-Mail', 'Breastplate',
        'Half-Plate-Armor', 'Ring-Mail', 'Chain-Mail', 'Splint-Armor', 'Plate-Armor'
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')

class LevelUpForm(FlaskForm):
    hp = IntegerField('Hit Points', validators=[DataRequired()])
    ability_score_1 = SelectField('Select an Ability Score to increase by 1', 
                                  choices=['-Please Choose-',
                                      'Strength', 'Dexterity', 'Constitution',
                                      'Intelligence', 'Wisdom', 'Charisma'
                                  ], validators=[Optional()], 
                                  default='-Please Choose-')
    ability_score_2 = SelectField('Select an Ability Score to increase by 1', 
                                  choices=['-Please Choose-',
                                      'Strength', 'Dexterity', 'Constitution',
                                      'Intelligence', 'Wisdom', 'Charisma'
                                  ], validators=[Optional()], 
                                  default='-Please Choose-')
    submit = SubmitField('Submit')

class SubclassForm(FlaskForm):
    subclass = SelectField('Subclass', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

class PactBoonForm(FlaskForm):
    pact_boon = SelectField('Pact Boon', choices=[
        '-Please Choose-', 'Pact-of-the-Chain', 'Pact-of-the-Blade', 
        'Pact-of-the-Tome'
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')

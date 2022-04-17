from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class NewCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    strength = SelectField('Strength', choices=[], coerce=int,
                           validate_choice=False, validators=[DataRequired()])
    dexterity = SelectField('Dexterity', choices=[], coerce=int, 
                            validate_choice=False, validators=[DataRequired()])
    constitution = SelectField('Constitution', choices=[], coerce=int,
                               validate_choice=False, validators=[DataRequired()])
    intelligence = SelectField('Intelligence', choices=[],  coerce=int,
                               validate_choice=False, validators=[DataRequired()])
    wisdom = SelectField('Wisdom', choices=[], coerce=int,
                         validate_choice=False, validators=[DataRequired()])
    charisma = SelectField('Charisma', choices=[], coerce=int,
                           validate_choice=False, validators=[DataRequired()])
    ancestry = SelectField('Ancestry', choices=[
        '-Please Choose-', 'Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn',
        'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling'
    ], validators=[DataRequired()])
    plustwo = SelectField('+2 to Which Ability Score? (Note: If you choose Human this will not apply)',
        choices=[
        '-Please Choose-', 'Strength', 'Dexterity', 'Constitution',
        'Intelligence', 'Wisdom', 'Charisma'
    ])
    plusone = SelectField('+1 to Which Ability Score? (Note: If you choose Human this will not apply)',
        choices=[
        '-Please Choose-', 'Strength', 'Dexterity', 'Constitution',
        'Intelligence', 'Wisdom', 'Charisma'
    ])
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

class EditCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    strength = SelectField('Strength', choices=[], validators=[DataRequired()])
    dexterity = SelectField('Dexterity', choices=[], validators=[DataRequired()])
    constitution = SelectField('Constitution', choices=[], validators=[DataRequired()])
    intelligence = SelectField('Intelligence', choices=[], validators=[DataRequired()])
    wisdom = SelectField('Wisdom', choices=[], validators=[DataRequired()])
    charisma = SelectField('Charisma', choices=[], validators=[DataRequired()])
    ancestry = SelectField('Ancestry', choices=[
        '-Please Choose-', 'Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn',
        'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling'
    ], validators=[DataRequired()])
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

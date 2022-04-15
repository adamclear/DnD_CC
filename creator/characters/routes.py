from creator import db
from creator.models import Character
from creator.characters.utils import get_class_features, get_char_traits, roll_stats
from creator.characters.forms import NewCharacterForm
from creator.users.utils import gen_id
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user
import json
import requests

characters = Blueprint('characters', __name__)


@characters.route('/new_character', methods=['GET', 'POST'])
def new_character():
    if current_user.is_authenticated:
        form = NewCharacterForm()
        stats = roll_stats()
        id = gen_id()
        if form.validate_on_submit():
            character = Character(id=id,
                                  name=form.name.data,
                                  stat1=stats[0],
                                  stat2=stats[1],
                                  stat3=stats[2],
                                  stat4=stats[3],
                                  stat5=stats[4],
                                  stat6=stats[5],
                                  strength=form.strength.data,
                                  dexterity=form.dexterity.data,
                                  constitution=form.constitution.data,
                                  intelligence=form.intelligence.data,
                                  wisdom=form.wisdom.data,
                                  charisma=form.charisma.data,
                                  ancestry=form.ancestry.data,
                                  heroic_class=form.heroic_class.data,
                                  weapon=form.weapon.data,
                                  armor=form.armor.data,
                                  player=current_user
                                  )
            db.session.add(character)
            db.session.commit()
            hp_roll = character.roll_hp()
            character.hp1 = hp_roll
            db.session.commit()
            flash(f'{character.name} has been created!')
            return redirect(url_for('characters.character_sheet', character_id=id))
    else:
        return redirect(url_for('users.login'))
    return render_template('new_character.html', title='New Character', form=form, stats=stats)

@characters.route('/my_characters', methods=['GET', 'POST'])
def view_characters():
    if current_user.is_authenticated:
        return render_template('my_characters.html', title='View Characters')
    else:
        return redirect(url_for('users.login'))

# will have to add an extension of the route below for character id/name/something
@characters.route('/<string:character_id>/character_sheet', methods=['GET', 'POST'])
def character_sheet(character_id):
    if current_user.is_authenticated:
        character = Character.query.get(character_id)
        feat_dict = get_class_features(character.id)
        trait_dict = get_char_traits(character.id)
        char_hp = character.calc_hp()
        char_ac = character.calc_ac()
        str_mod = character.calc_mod(character.strength)
        dex_mod = character.calc_mod(character.dexterity)
        con_mod = character.calc_mod(character.constitution)
        int_mod = character.calc_mod(character.intelligence)
        wis_mod = character.calc_mod(character.wisdom)
        cha_mod = character.calc_mod(character.charisma)
        return render_template('character_sheet.html', title='Character Sheet', 
                               character=character, feat_dict=feat_dict,
                               trait_dict=trait_dict, char_hp=char_hp,
                               str_mod=str_mod, dex_mod=dex_mod,
                               con_mod=con_mod, int_mod=int_mod,
                               wis_mod=wis_mod, cha_mod=cha_mod,
                               char_ac=char_ac)
    else:
        return redirect(url_for('users.login'))

# will have to add an extension of the route below for character id/name/something
@characters.route('/edit_character', methods=['GET', 'POST'])
def edit_character():
    if current_user.is_authenticated:
        # add conditional to check for if character id is owned by the current user id
        return render_template('edit_character.html', title='Edit Character')
    else:
        return redirect(url_for('users.login'))

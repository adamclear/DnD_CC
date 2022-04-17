from creator import db
from creator.models import Character
from creator.characters.utils import (get_armor_info, get_class_features, 
                                      get_char_traits, get_weapon_info, roll_stats)
from creator.characters.forms import EditCharacterForm, NewCharacterForm
from creator.users.utils import gen_id
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user

characters = Blueprint('characters', __name__)


@characters.route('/new_character', methods=['GET', 'POST'])
def new_character():
    if current_user.is_authenticated:
        form = NewCharacterForm()
        stats = roll_stats()
        id = gen_id()
        choices_list = [0]
        for x in stats:
            choices_list.append(x)
        form.strength.choices=choices_list
        form.dexterity.choices=choices_list
        form.constitution.choices=choices_list
        form.intelligence.choices=choices_list
        form.wisdom.choices=choices_list
        form.charisma.choices=choices_list
        plus_two = form.plustwo.data
        plus_one = form.plusone.data
        if form.validate_on_submit():
            character = Character(id=id,
                                  name=form.name.data,
                                  stat1=stats[0],
                                  stat2=stats[1],
                                  stat3=stats[2],
                                  stat4=stats[3],
                                  stat5=stats[4],
                                  stat6=stats[5],
                                  strength=int(form.strength.data),
                                  dexterity=int(form.dexterity.data),
                                  constitution=int(form.constitution.data),
                                  intelligence=int(form.intelligence.data),
                                  wisdom=int(form.wisdom.data),
                                  charisma=int(form.charisma.data),
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
            if character.ancestry == 'Human':
                character.strength += 1
                character.dexterity += 1
                character.constitution += 1
                character.intelligence += 1
                character.wisdom += 1
                character.charisma += 1
            else:
                plus_two_exec = 'character.' + str(plus_two.lower()) + ' += 2'
                plus_one_exec = 'character.' + str(plus_one.lower()) + ' += 1'
                exec(plus_two_exec)
                exec(plus_one_exec)
            db.session.commit()
            flash(f'{character.name} has been created!', 'success')
            return redirect(url_for('characters.character_sheet', character_id=id))
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))
    return render_template('new_character.html', title='New Character',
                           form=form, stats=stats)

@characters.route('/my_characters', methods=['GET', 'POST'])
def my_characters():
    if current_user.is_authenticated:
        return render_template('my_characters.html', title='My Characters')
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))

@characters.route('/<string:character_id>/character_sheet', methods=['GET', 'POST'])
def character_sheet(character_id):
    if current_user.is_authenticated:
        character = Character.query.get(character_id)
        feat_dict = get_class_features(character.id)
        trait_dict = get_char_traits(character.id)
        weapon_dict = get_weapon_info(character.id)
        armor_dict = get_armor_info(character.id)
        char_hp = character.calc_hp()
        char_ac = character.calc_ac()
        prof_bonus = character.calc_prof()
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
                               char_ac=char_ac, prof_bonus=prof_bonus,
                               armor_dict=armor_dict, weapon_dict=weapon_dict)
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))

@characters.route('/<string:character_id>/edit_character', methods=['GET', 'POST'])
def edit_character(character_id):
    if current_user.is_authenticated:
        character = Character.query.get(character_id)
        if character.player != current_user:
            flash(f"{character.name} doesn't belong to you!")
            return redirect(url_for('characters.my_characters'))
        else:
            form = EditCharacterForm()
            stats = [character.stat1, character.stat2, character.stat3,
                     character.stat4, character.stat5, character.stat6]
            if form.validate_on_submit():
                character.name = form.name.data
                character.strength = form.strength.data
                character.dexterity = form.dexterity.data
                character.constitution = form.constitution.data
                character.intelligence = form.intelligence.data
                character.wisdom = form.wisdom.data
                character.charisma = form.charisma.data
                character.ancestry = form.ancestry.data
                character.heroic_class = form.heroic_class.data
                character.weapon = form.weapon.data
                character.armor = form.armor.data
                db.session.commit()
                flash(f'{character.name} has been updated!', 'success')
                return redirect(url_for('characters.character_sheet',
                                        character_id=character.id))
            elif request.method == 'GET':
                form.name.data = character.name
                form.strength.data = character.strength
                form.dexterity.data = character.dexterity
                form.constitution.data = character.constitution
                form.intelligence.data = character.intelligence
                form.wisdom.data = character.wisdom
                form.charisma.data = character.charisma
                form.ancestry.data = character.ancestry
                form.heroic_class.data = character.heroic_class
                form.weapon.data = character.weapon
                form.armor.data = character.armor
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))
    return render_template('edit_character.html', title=f'Edit {character.name}',
                           form=form, character=character, stats=stats)

@characters.route('/<string:character_id>/level_up', methods=['GET', 'POST'])
def level_up(character_id):
    if current_user.is_authenticated:
        character = Character.query.get(character_id)
        if character.player != current_user:
            flash(f"{character.name} doesn't belong to you!")
            return redirect(url_for('characters.my_characters'))
        else:
            level = character.level
            if level == 20:
                flash(f'{character.name} is already max level!', 'danger')
                return redirect(url_for('characters.character_sheet',
                            character_id=character.id))
            level += 1
            character.level = level
            hp_roll = character.roll_hp()
            program = 'character.hp' + str(level) + ' = ' + 'hp_roll'
            exec(program)
            db.session.commit()
            flash(f'Leveled up! {character.name} is now level {character.level}.', 'success')
            return redirect(url_for('characters.character_sheet',
                            character_id=character.id))
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))

@characters.route('/<string:character_id>/delete', methods=['GET', 'POST'])
def delete(character_id):
    if current_user.is_authenticated:
        character = Character.query.get(character_id)
        if character.player != current_user:
            flash(f"{character.name} doesn't belong to you!")
            return redirect('characters.my_characters')
        else:
            db.session.delete(character)
            db.session.commit()
            flash(f'{character.name} was deleted!', 'success')
            return redirect(url_for('characters.my_characters'))
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))

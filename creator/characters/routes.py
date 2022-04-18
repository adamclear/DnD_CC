from creator import db
from creator.models import Character
from creator.characters.utils import (get_armor_info, get_class_features, 
                                      get_char_traits, get_subclass_features, 
                                      get_weapon_info, roll_stats)
from creator.characters.forms import (AbilityScoreForm, AbilityScoreFormHuman, 
                                      EditCharacterForm, LevelUpForm, 
                                      NewCharacterForm, SubclassForm)
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
        if form.validate_on_submit():
            character = Character(id=id,
                                  name=form.name.data,
                                  ancestry=form.ancestry.data,
                                  heroic_class=form.heroic_class.data,
                                  weapon=form.weapon.data,
                                  armor=form.armor.data,
                                  player=current_user
                                  )
            db.session.add(character)
            db.session.commit()
            character.hp1 = character.roll_hp()
            db.session.commit()
            flash(f"{character.name} has been created!", 'success')
            return redirect(url_for('characters.ability_scores', character_id = id))
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))
    return render_template('new_character.html', title='New Character',
                           form=form, stats=stats)

@characters.route('/<string:character_id>/ability_scores', methods=['GET', 'POST'])
def ability_scores(character_id):
    if current_user.is_authenticated:
        character = Character.query.get(character_id)
        if character.player != current_user:
            flash(f"{character.name} doesn't belong to you!")
            return redirect(url_for('characters.my_characters'))
        else:
            stats = roll_stats()
            if character.ancestry == 'Human':
                form = AbilityScoreFormHuman()
                human = True
                if form.validate_on_submit():
                    character.stat1 = stats[0]
                    character.stat2 = stats[1]
                    character.stat3 = stats[2]
                    character.stat4 = stats[3]
                    character.stat5 = stats[4]
                    character.stat6 = stats[5]
                    character.strength = form.strength.data + 1
                    character.dexterity = form.dexterity.data + 1
                    character.constitution = form.constitution.data + 1
                    character.intelligence = form.intelligence.data + 1
                    character.wisdom = form.wisdom.data + 1
                    character.charisma = form.charisma.data + 1
                    if character.heroic_class == 'Sorcerer' or character.heroic_class == 'Warlock':
                        db.session.commit()
                        flash(f'{character.name} gets to choose a subclass at level {character.level}.',
                            'success')
                        return redirect(url_for('characters.subclass_choice', character_id=character.id))
                    else:
                        db.session.commit()
                        flash(f'{character.name} has been created!', 'success')
                        return redirect(url_for('characters.character_sheet', character_id=character.id))
            else:
                form = AbilityScoreForm()
                plus_two = form.plustwo.data
                plus_one = form.plusone.data
                human = False
                if form.validate_on_submit():
                    character.stat1 = stats[0]
                    character.stat2 = stats[1]
                    character.stat3 = stats[2]
                    character.stat4 = stats[3]
                    character.stat5 = stats[4]
                    character.stat6 = stats[5]
                    character.strength = form.strength.data
                    character.dexterity = form.dexterity.data
                    character.constitution = form.constitution.data
                    character.intelligence = form.intelligence.data
                    character.wisdom = form.wisdom.data
                    character.charisma = form.charisma.data
                    exec('character.' + str(plus_two.lower()) + ' += 2')
                    exec('character.' + str(plus_one.lower()) + ' += 1')
                    db.session.commit()
                    if character.heroic_class == 'Sorcerer' or character.heroic_class == 'Warlock':
                        flash(f'{character.name} gets to choose a subclass at level {character.level}.',
                            'success')
                        return redirect(url_for('characters.subclass_choice', character_id=character.id))
                    else:
                        flash(f'{character.name} has been created!', 'success')
                        return redirect(url_for('characters.character_sheet', character_id=character.id))
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))
    return render_template('ability_scores.html', 
                           title=f"{character.name}'s Ability Scores",
                           form=form, stats=stats, human=human)

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
        if character.subclass:
            subclass_dict = get_subclass_features(character.id)
        else:
            subclass_dict = None
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
                               armor_dict=armor_dict, weapon_dict=weapon_dict,
                               subclass_dict=subclass_dict)
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
            if form.validate_on_submit():
                character.name = form.name.data
                character.weapon = form.weapon.data
                character.armor = form.armor.data
                db.session.commit()
                flash(f'{character.name} has been updated!', 'success')
                return redirect(url_for('characters.character_sheet',
                                        character_id=character.id))
            elif request.method == 'GET':
                form.name.data = character.name
                form.weapon.data = character.weapon
                form.armor.data = character.armor
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))
    return render_template('edit_character.html', title=f'Edit {character.name}',
                           form=form, character=character)

@characters.route('/<string:character_id>/level_up', methods=['GET', 'POST'])
def level_up(character_id):
    if current_user.is_authenticated:
        character = Character.query.get(character_id)
        if character.player != current_user:
            flash(f"{character.name} doesn't belong to you!")
            return redirect(url_for('characters.my_characters'))
        else:
            form = LevelUpForm()
            level = character.level
            if level == 20:
                flash(f'{character.name} is already max level!', 'danger')
                return redirect(url_for('characters.character_sheet',
                                character_id=character.id))
            level += 1
            character.level = level
            if level in [4, 8, 12, 16, 19]:
                asi = True
            else:
                asi = False
            hp_roll = character.roll_hp()
            if form.validate_on_submit():
                program = 'character.hp' + str(level) + ' = ' + str(form.hp.data)
                exec(program)
                if form.ability_score_1.data != '-Please Choose-':
                    asi1_exec = 'character.' + str(form.ability_score_1.data.lower()) + ' += 1'
                    exec(asi1_exec)
                if form.ability_score_2.data != '-Please Choose-':
                    asi2_exec = 'character.' + str(form.ability_score_2.data.lower()) + ' += 1'
                    exec(asi2_exec)
                level_2_subclasses = [
                    'Cleric', 'Druid', 'Wizard'
                ]
                level_3_subclasses = [
                    'Barbarian', 'Bard', 'Fighter', 'Monk',
                    'Paladin', 'Ranger', 'Rogue'
                ]
                db.session.commit()
                if character.heroic_class in level_2_subclasses and character.level == 2:
                    flash(f'{character.name} gets to choose a subclass at level {character.level}.',
                        'success')
                    return redirect(url_for('characters.subclass_choice', character_id=character.id))
                elif character.heroic_class in level_3_subclasses and character.level == 3:
                    flash(f'{character.name} gets to choose a subclass at level {character.level}.',
                        'success')
                    return redirect(url_for('characters.subclass_choice', character_id=character.id))
                elif character.heroic_class == 'Warlock' and character.level == 3:
                    flash(f'{character.name} gets to choose a Pact Boon at level {character.level}.',
                        'success')
                    return redirect(url_for('characters.pact_boon_choice', character_id=character.id))
                else:
                    flash(f'Leveled up! {character.name} is now level {character.level}.',
                        'success')
                    return redirect(url_for('characters.character_sheet',
                                    character_id=character.id))
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))
    return render_template('level_up.html', title=f'Level up {character.name}',
                           form=form, character=character, hp_roll=hp_roll,
                           asi=asi)

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

@characters.route('/<string:character_id>/subclass_choice', methods=['GET', 'POST'])
def subclass_choice(character_id):
    if current_user.is_authenticated:
        form = SubclassForm()
        character = Character.query.get(character_id)
        if character.player != current_user:
            flash(f"{character.name} doesn't belong to you!")
            return redirect('characters.my_characters')
        else:
            subclass_dict = {
                'Barbarian': 'Berserker',
                'Bard': 'Lore',
                'Cleric': 'Life',
                'Druid': 'Land',
                'Fighter': 'Champion',
                'Monk': 'Open-Hand',
                'Paladin': 'Devotion',
                'Ranger': 'Hunter',
                'Rogue': 'Thief',
                'Sorcerer': 'Draconic',
                'Warlock': 'Fiend',
                'Wizard': 'Evocation'
            }
            form.subclass.choices.append(subclass_dict[character.heroic_class])
            if form.validate_on_submit():
                if character.level != 1:
                    character.subclass = form.subclass.data
                    db.session.commit()
                    flash('Subclass chosen!', 'success')
                    return redirect(url_for('characters.character_sheet',
                                    character_id=character.id))
                else:
                    character.subclass = form.subclass.data
                    db.session.commit()
                    flash('Subclass chosen!', 'success')
                    return redirect(url_for('characters.character_sheet', 
                                    character_id=character.id))
    else:
        flash('Please login', 'danger')
        return redirect(url_for('users.login'))
    return render_template('subclass.html', title=f"{character.name}'s Subclass", 
                           form=form, character_id=character.id)

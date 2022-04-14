from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user

characters = Blueprint('characters', __name__)


@characters.route('/new_character', methods=['GET', 'POST'])
def new_character():
    if current_user.is_authenticated:
        return render_template('new_character.html', title='New Character')
    else:
        return redirect(url_for('users.login'))

@characters.route('/view_all_characters', methods=['GET', 'POST'])
def view_characters():
    if current_user.is_authenticated:
        return render_template('new_character.html', title='View Characters')
    else:
        return redirect(url_for('users.login'))

# will have to add an extension of the route below for character id/name/something
@characters.route('/character_sheet', methods=['GET', 'POST'])
def character_sheet():
    if current_user.is_authenticated:
        return render_template('character_sheet.html', title='Character Sheet')
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

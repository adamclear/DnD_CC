from flask import Blueprint, render_template
from flask import redirect, url_for
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    """
    Method to render the home page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('characters.my_characters'))
    return render_template('home.html')

@main.route("/about")
def about():
    return render_template('about.html', title='About')

from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    """
    Method to render the home page.
    """
    return render_template('home.html')

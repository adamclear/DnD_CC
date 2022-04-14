from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    """
    Method to render the home page.
    """
    return render_template('home.html')

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/create_new")
def create():
    return render_template('create_new.html', title='Create')

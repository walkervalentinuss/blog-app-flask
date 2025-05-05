from flask import Blueprint, render_template

# Create views blueprint
views = Blueprint("views", __name__)

# Create home route
@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", name='Home')

@views.route("/login")
def login():
    return render_template("login.html", name='Login')

@views.route("/sign-up")
def signup():
    return render_template("signup.html", name='Sign Up')
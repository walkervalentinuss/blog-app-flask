from flask import Blueprint, render_template

# Create auth blueprint
auth = Blueprint("auth", __name__)

# Create login route
@auth.route("/login")
def login():
    return "login"

# Create sign up route
@auth.route("/sign-up")
def sign_up():
    return "sign up"

# Create logout route
@auth.route("/logout")
def logout():
    return "logout"
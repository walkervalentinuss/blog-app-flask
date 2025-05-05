# Prerequisite
- python intermediate
- python 3.8 or another version > 3.6
- Basic knowledge of HTML and HTTP

# Create env
"C:\Users\walkervalentinus\AppData\Local\Programs\Python\Python38\python.exe" -m venv env

# Activate env
env\Scripts\activate.bat

# Deactivate env
deactivate

# Run the app
``` python .\app.py```

# Libraries Used
- Flask
- Flask-SQLAlchemy
or simply `pip install -r requirements.txt`

# Create Blueprint for organized code
- `views.py` in `website` folder for things related to views like hompage, user profile, etc, here we also storing every routes used in the app.
- `auth.py` in `website` folder for things related to authentication like login, signup, etc.

# Flask Agenda Templating Engine `Jinja`
this is the main reason why we don't use javascript for creating this project, to use this templating engine we need a '{{  }}' to indicate that this is a jinja template, so we can pass a variable from aour backend to our fronted. Also, we can use '{% %}' for control flow like if, for, etc. Last one is '{# #}' for comments.

## Template Inheritance
We can have templates inherits from other templates, so we can have a base template to save design like the navbar, footer, etc.
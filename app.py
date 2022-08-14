"""
app.py

Main App application

Jose Guzman, sjm.guzman@gmail.com
Created: Fri Aug 12 19:37:32 EDT 2022

"""
from unicodedata import name
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

# forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, Email

# database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__, template_folder = 'templates', static_url_path = '/static')
app.config["SECRET_KEY"] = b'_5#y2L"F4Q8z\n\xec]/'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db" # database location

Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class LoginForm(FlaskForm):
    """ user/pass login"""
    email = StringField("E-mail", validators = [ Email() ])
    passwd = PasswordField("Password", validators = [ Length(min=8) ] )

class RegistrationForm(FlaskForm):
    """ registration involves name and institution/company """
    name = StringField("First name", validators = [ Length(min=4, max =20) ])
    surname = StringField("Last name", validators = [ Length(min=4, max =20) ])
    email = StringField("E-mail", validators = [ Email() ])
    passwd = PasswordField("Password", validators = [ Length(min=8) ] )
    passwd2 = PasswordField("Confirm password", validators = [ Length(min=8) ] )
    project = StringField("Brief project description", validators = [ Length(max=280) ])
     

# Models are to map tables in db to python objects

class User(db.Model):
    name = db.Column( db.String(128) )
    surname = db.Column( db.String(128) ) 
    email = db.Column( db.String(128) )
    passwd = db.Column( db.String(128), primary_key = True )
    project = db.Column( db.String(280) )
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    """
    The Login form
    """
    loginform = LoginForm()

    if loginform.validate_on_submit():
        return "It's valid"

    return render_template("login.html", form = loginform)

@app.route("/register", methods = ["GET", "POST"])
def register():
    """
    The Register form
    """
    registerform = RegistrationForm()

    if registerform.validate_on_submit():
        return "It's valid"

    return render_template("register.html", form = registerform)

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run( debug = True ) # export FLASK_DEBUG=1

"""
app.py

Main App application

Jose Guzman, sjm.guzman@gmail.com
Created: Fri Aug 12 19:37:32 EDT 2022

"""
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    # in templates/index.html
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

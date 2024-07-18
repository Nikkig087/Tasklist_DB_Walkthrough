from flask import render_template
from taskmanager import app, db

# This will be used to target a function called 'home', which will just return the rendered_template of "base.html" that we will create shortly.
@app.route("/")
def home():
    return render_template("base.html")
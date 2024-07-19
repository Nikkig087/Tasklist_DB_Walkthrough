from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager import app, db
from taskmanager.models import Category, Task

# This will be used to target a function called 'home', which will just return the rendered_template of "base.html" that we will create shortly.
@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


# as we are submitting a form we need to have this
@app.route("/add_category",methods=["GET","POST"])
def add_category():
    if request.method == "POST":
        # we need to make sure the model uses the same keys as stated in models.py
        category = Category(category_name =request.form.get("category_name"))
        db.session.add(category) # posting to db
        db.session.commit() # posting to db
        return redirect(url_for("categories")) #redirect back to categories
    return render_template("add_category.html") # this is the get part can be considered as an else if the above doesnt happen
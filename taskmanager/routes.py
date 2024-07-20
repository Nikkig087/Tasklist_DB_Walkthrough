from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager import app, db
from taskmanager.models import Category, Task

# This will be used to target a function called 'home', which will just return the rendered_template of "base.html" that we will create shortly.
@app.route("/")
def home():
    return render_template("tasks.html")

# Whenever we call this function by clicking the navbar link for Categories, it will query the database and retrieve all records from this table, then sort them by the category name.
@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all()) # queries tha Category model on line 4
    return render_template("categories.html", categories = categories) # 1st categories comes from categories html and the second comes from our varible here in this block


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

#we know our ids will be ints so we cast that here <int>
@app.route("/edit_category/<int:category_id>",methods=["GET","POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id) #queries the db and expects to find the specified record using data provided
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)
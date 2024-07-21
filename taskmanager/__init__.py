import re
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env    # noqa

# in order to use our hidden enviroment varibles we need to import the env package
# We are not pushing this file to github so if we deployed to heroku we would get an error

# we only import env if the os can find an existing file path for the env.py file itself
if os.path.exists("env.py"):
    import env #noqa


#create an instance of the imported Flask() class


#app = Flask(__name__) # default name module

#the below are set to their enviroment varible
#app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
#app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app) #instance of SQLAlchemy class

from taskmanager import routes  # noqa
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #pip install Flask_Migrate

#create sqlite database using python in flask
basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ is the pathname of file from which the module where __file__ is called, was loaded. If you call __file__ from within a .py file, say, foo.py, then __file__ will contain the path of foo.py on your disk.
# os.path.dirname(path)
# Return Type: This method returns a string value which represents the directory name from the specified path.

# According to docs os.path.abspath() returns a normalized absolutized version of
# the pathname path which may sound fancy but it simply means that this method returns the pathname to the path passed
#  as a parameter to this function.
#  his method returns a normalized version of the pathname path.


#What we're doing here is we're saying that we want to create a database.
# We need to pass in the base directory that we want it to go, and then we want it to be named app.sqlite. Now that we have that, we
# can create a database object.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create database object
#passing ur app through sqlalchemy
db = SQLAlchemy(app)
# app.app_context().push()

Migrate(app,db)
#create a model(setting up a table in a databse)
class Puppy(db.Model):

#DEFAULT TABLE NAME IS PROVIDED WITH THE CLASS name
#Create the new table name but: manual
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year's old"

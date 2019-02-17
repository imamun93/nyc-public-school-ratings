# import Flask and jsonify from flask
from flask import Flask, render_template, jsonify

# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# initialize new flask app
app = Flask(__name__)

# tell your flask app to run with debug mode on
app.config['DEBUG'] = True


# add configurations and database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'


# connect SQLAlchemy to the configured flask app
db = SQLAlchemy(app)


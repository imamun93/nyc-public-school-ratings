from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

class School(db.Model):
	__tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    dbn = db.Column(db.String, unique=True, nullable=False)
	name= db.Column(db.String, nullable= False)


class SchoolSAT(db.Model):
	__tablename__ = 'school_culturess'

	id = db.Column(db.Integer, primary_key=True)
	year = db.Column(db.DateTime, nullable=False)
	#belongs to a school
	dbn = db.Column(db.String, nullable=False )
	math_avg = db.Column(db.Integer, nullable=False)
	reading_avg = db.Column(db.Integer, nullable=False)
	overall_avg = db.Column(db.Integer, nullable=False)



app = Flask(__name__)
    # add configurations and database URI
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


# db = SQLAlchemy(app)
# from dash_package import app
import dash_core_components as dcc
import dash_html_components as html

from dash_package.models import *
def sat_avg():
    name=[]
    math=[]
    read=[]
    for school in School.query.all():
        if school.sats:
            name.append(school.name)
            math.append(school.sats[0].math_avg)
            read.append(school.sats[0].reading_avg)
    return [{'x': name, 'y': math, 'type': 'bar', 'name': 'math avgs'}, {'x': name, 'y': read, 'type': 'bar', 'name': 'reading avgs'}]

def overall_rating():
    school_name=[]
    overall_rating=[]
    no_rating=[]
    for school in School.query.all():
        if school.ratings:
            school_name.append(school.name)
            overall_rating.append(school.ratings[0].overall)
    return [{'x': school_name, 'y': overall_rating, 'type': 'bar', 'name': 'school_ratings'}]




#
# def math_avgs():
#     math_avgs=[]
#     for i in School.query.all():
#         math_avgs.append(i.sat[0].math_avg)
#     return math avgs



# from flask import Flask
# # import SQLAlchemy from flask_sqlalchemy
# from flask_sqlalchemy import SQLAlchemy
# # from models import *
# # initialize new flask app
# app = Flask(__name__)
# #
# # # tell your flask app to run with debug mode on
# app.config['DEBUG'] = True
# #
# #
# # add configurations and database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# #
# #
# # connect SQLAlchemy to the configured flask app
# db= SQLAlchemy(app)
#
#
# # {'dbn': '01M292', 'school_name': 'HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES', 'test_takers': '29', 'reading_avg': '355', 'math_avg': '404', 'writing_avg': '363'}, {'dbn': '01M448', 'school_name': 'UNIVERSITY NEIGHBORHOOD HIGH SCHOOL', 'test_takers': '91', 'reading_avg': '383', 'math_avg': '423', 'writing_avg': '366'},

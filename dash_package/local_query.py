# db = SQLAlchemy(app)
import pdb
from local_models import *
def school_rating_sat():
    math_avgs= [i.sats[0].math_avg for i in School.query.all()]
#     school_names= [i.name for i in School.query.all()]
#     school_rating = [i.overall for i in db.session.query(Rating).all()]
#     return {'X': school_rating}

def sat_avg():
    name=[]
    math=[]
    for school in School.query.all():
        if school.sats[0].math_avg:
            name.append(school.name)
            math.append(school.sats[0].math_avg)
    return {'x': name, 'y': math, 'type': 'bar', 'name': 'Math Avgs'}

def overall_rating():
    school_name=[]
    overall_rating=[]
    for school in School.query.all():
        if school.ratings:
            if school.ratings[0].overall:
                school_name.append(school.name)
                print(school.id, school.ratings[0].overall)
                overall_rating.append(school.ratings[0].overall)
    return overall_rating
    # return {'x': school_name, 'y': overall_rating, 'type': 'bar', 'name': 'school_ratings'}


def load_total_attendance():
    for ay in Attendance_Year.query.all(): 
        ay.total_absent = ay.grade_9_absent + ay.grade_10_absent + ay.grade_11_absent + ay.grade_12_absent
        ay.total_present = ay.grade_9_present + ay.grade_10_present + ay.grade_11_present + ay.grade_12_present
        db.session.add(ay) 
        db.session.commit()




from flask import Flask
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# from models import *
# initialize new flask app
app = Flask(__name__)
#
# # tell your flask app to run with debug mode on
app.config['DEBUG'] = True
#
#
# add configurations and database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#
# connect SQLAlchemy to the configured flask app
db= SQLAlchemy(app)



# {'dbn': '01M292', 'school_name': 'HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES', 'test_takers': '29', 'reading_avg': '355', 'math_avg': '404', 'writing_avg': '363'}, {'dbn': '01M448', 'school_name': 'UNIVERSITY NEIGHBORHOOD HIGH SCHOOL', 'test_takers': '91', 'reading_avg': '383', 'math_avg': '423', 'writing_avg': '366'},

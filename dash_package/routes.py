from flask import render_template
from dash_package.models import *
from dash_package import server

@server.route('/school')
def render_school():
    school= School.query.get(1)
    return school.name

# from dash_package import app2
# from dash_package.query import *
# import pdb
#
#
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objs as go
# import plotly.plotly as py
#
# from dash_package.mega_data import mega_list_2012, mega_list_2013, mega_list_2014, mega_list_2015, mega_list_2016, mega_list_2017
#
# def sat_avg():
# 	name=[]
# 	math=[]
# 	read=[]
# 	for school in School.query.all():
# 		if school.sats:
# 			name.append(school.name)
# 			math.append(school.sats[0].math_avg)
# 			read.append(school.sats[0].reading_avg)
# 	return [{'x': name, 'y': math, 'type': 'bar', 'name': 'math avgs'}, {'x': name, 'y': read, 'type': 'bar', 'name': 'reading avgs'}]
#
# def overall_rating():
# 	school_name=[]
# 	overall_rating=[]
# 	no_rating=[]
# 	for school in School.query.all():
# 		if school.ratings:
# 			school_name.append(school.name)
# 			overall_rating.append(school.ratings[0].overall)
# 	return [{'x': school_name, 'y': overall_rating, 'type': 'bar', 'name': 'school_ratings'}]
#
# school_names = []
# school_math_sats = []
# school_reading_sats = []
# school_ratings = []
#
# def school_rating_for_year(school_obj, year):
# 	school = School.query.filter(School.id == school_obj.id).first()
# 	for rating in school.ratings:
# 		if rating.year == year:
# 			return rating.overall
# 		else:
# 			return "0"
#
# def most_recent_rating(school_obj):
# 	school = School.query.filter(School.id == school_obj.id).first()
# 	if school.ratings:
# 		current_year = 0
# 		most_recent = [0]
# 		for rating in school.ratings:
# 			if rating.year > current_year and rating.overall:
# 				current_year = rating.year
# 				most_recent[0] = rating
# 		if most_recent[0].overall == 'None':
# 			return 0
# 		return most_recent[0].overall
# 	else:
# 		return 0
#
# def most_recent_rating_year(school_obj):
# 	school = School.query.filter(School.id == school_obj.id).first()
# 	if school.ratings:
# 		current_year = 0
# 		most_recent = [0]
# 		for rating in school.ratings:
# 			if rating.year > current_year and rating.overall:
# 				current_year = rating.year
# 				most_recent[0] = rating
# 		return most_recent[0].year
#
#
#
#
#
# def school_sats_year(school_obj, year):
# 	school = School.query.filter(School.id == school_obj.id).first()
# 	if school.sats:
# 		return [school.sats[0].math_avg, school.sats[0].reading_avg]
# 	else:
# 		return [0, 0]
#
# def sats_rating_year_data(year):
# 	school_names = []
# 	school_math_sats = []
# 	school_reading_sats = []
# 	school_ratings = []
# 	for school in School.query.all():
# 		if not school.ratings and not school.sats:
# 			continue
# 		else:
# 			sats = school_sats_year(school, year)
# 			school_math_sats.append(sats[0])
# 			school_reading_sats.append(sats[1])
# 			rating = school_rating_for_year(school, year)
# 			school_ratings.append(rating)
# 			school_names.append(school.name)
# 	return [school_names, school_math_sats, school_reading_sats, school_ratings]
#
# def attendance_percentage_school_year(school_obj, year):
# 	school = School.query.filter(School.id == school_obj.id).first()
# 	response = 0
# 	if school.attendance_years:
# 		for ay in school.attendance_years:
# 			if ay.year == year and ay.total_absent != 0 and ay.total_present != 0:
# 				response = round(float(ay.total_absent/ay.total_present), 3)
# 	return response
#
#
#
#
# def sats_attendance_year_rating_data(year):
# 	school_names = []
# 	school_math_sats = []
# 	school_reading_sats = []
# 	school_attendance = []
# 	school_recent_rating = []
# 	for school in School.query.all():
# 		if not school.attendance_years and not school.sats:
# 			continue
# 		else:
# 			sats = school_sats_year(school, year)
# 			school_math_sats.append(sats[0])
# 			school_reading_sats.append(sats[1])
# 			attendance_ratio = attendance_percentage_school_year(school, year)
# 			school_attendance.append(attendance_ratio)
# 			school_names.append(school.name)
# 			rating = most_recent_rating(school)
# 			school_recent_rating.append(rating)
# 	return [school_names, school_math_sats, school_reading_sats, school_attendance, school_recent_rating]
#
# # mega_list_2012 = sats_attendance_year_rating_data(2012)
# # mega_list_2013 = sats_attendance_year_rating_data(2013)
# # mega_list_2014 = sats_attendance_year_rating_data(2014)
# # mega_list_2015 = sats_attendance_year_rating_data(2015)
# # mega_list_2016 = sats_attendance_year_rating_data(2016)
# # mega_list_2017 = sats_attendance_year_rating_data(2017)
#
# # mega_list_2016s = sats_rating_year_data(2016)
#
# # print("mega_list_2012 = ", mega_list_2012)
# # print("mega_list_2013 = ", mega_list_2013)
# # print("mega_list_2014 = ", mega_list_2014)
# # print("mega_list_2015 = ", mega_list_2015)
# # print("mega_list_2016 = ", mega_list_2016)
# # print("mega_list_2017 = ", mega_list_2017)
#
#
#
# # mega_list_2012 = sats_rating_year_data(2012)
# # mega_list_2013 = sats_rating_year_data(2013)
# # mega_list_2014 = sats_rating_year_data(2014)
# # mega_list_2015 = sats_rating_year_data(2015)
# # pdb.set_trace()
#
#
#
# # school_rating = [i.overall for i in db.session.query(Rating).all()]
# # school_sat= School=[i.math_avg for i in db.session.query(SchoolSAT).all()]
#
# # def sat_avg():
# #     name=[]
# #     math=[]
# #     for school in School.query.all():
# #         if school.sats[0].math_avg:
# #             name.append(school.name)
# #             math.append(school.sats[0].math_avg)
# #     return {'x': name, 'y': math, 'type': 'bar', 'name': 'Math Avgs'}
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# ratings = ['1', '2' ,'3', '4']
#
# app2.layout = html.Div(children=[
# dcc.Tabs(id="tabs", children=[
# 	dcc.Tab(id='sat', label='Math AVG SAT',
# 		children=[
# 	dcc.Graph(
# 		id='math_avg_sat',
# 		figure={
# 			'data': [
# 				go.Scatter(
# 					x= mega_list_2013[1],
# 					y= mega_list_2013[3],
# 					text= mega_list_2013[0],
# 					mode='markers',
# 					opacity=0.7,
# 					marker={
# 						'size': 15,
# 						'line': {'width': 0.5, 'color': 'white'}
# 					},
# 					name=i
# 				) for i in ratings
# 			],
# 			'layout': go.Layout(
# 				xaxis={'type': 'log', 'title': 'Sat Scores - Math'},
# 				yaxis={'title': 'Absent:Present Ratio'},
# 				margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
# 				legend={'x': 0, 'y': 1},
# 				hovermode='closest')}
# 			)]
# 		),
# 		dcc.Tab(id='rat', label='READING AVG SAT',
#             children=[
#         dcc.Graph(
# 			id='read_avg_sat',
# 			figure=
# 				{'data': [
# 					go.Scatter(
# 						x= mega_list_2013[2],
# 						y= mega_list_2013[3],
# 						text= mega_list_2013[0],
# 						mode= 'markers',
# 						opacity= 0.7,
# 						marker={
# 							'size': 15,
# 							'line': {'width': 0.5, 'color': 'white'}
# 						},
# 						name= i
# 					) for i in ratings
# 				],
# 				'layout': go.Layout(
# 					xaxis={'type': 'log', 'title': 'Sat Scores - Read'},
# 					yaxis={'title': 'Absent:Present Ratio'},
# 					margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
# 					legend={'x': 0, 'y': 1},
# 					hovermode='closest')}
# 					)
# 				])
# 			])
# 		])
#
#
#
#
# # app.layout = html.Div(
# #     children=[
# #     dcc.Tabs(id="tabs", children=[
# #         dcc.Tab(id='sat', label='sat for 2012',
# #             children=[
# #             dcc.Graph(figure=
# #             {'data': sat_avg(),
# #             'layout': {}})
# #             ]
# #         ),
# #         dcc.Tab(id='rating', label='School Ratings',
# #             children=[
# #             dcc.Graph(figure=
# #             {'data': overall_rating(),
# #             'layout': {}})
# #             ]
# #         )
#
# #         ])
# #     ]
# # )
# def reset_total_attendance():
# 	for ay in Attendance_Year.query.all():
# 		ay.total_absent = 0
# 		ay.total_present = 0
# 		db.session.add(ay)
# 		db.session.commit()
#
# # reset_total_attendance()
# def load_total_attendance():
# 	for ay in Attendance_Year.query.all():
# 		if ay.grade_9_absent:
# 			ay.total_absent += ay.grade_9_absent
# 			ay.total_present += ay.grade_9_present
# 		if ay.grade_10_absent:
# 			ay.total_absent += ay.grade_10_absent
# 			ay.total_present += ay.grade_10_present
# 		if ay.grade_11_absent:
# 			ay.total_absent += ay.grade_11_absent
# 			ay.total_present += ay.grade_11_present
# 		if ay.grade_12_absent:
# 			ay.total_absent += ay.grade_12_absent
# 			ay.total_present += ay.grade_12_present
# 		db.session.add(ay)
# 		db.session.commit()
#
# # load_total_attendance()
# 		# ay.total_absent = ay.grade_9_absent + ay.grade_10_absent + ay.grade_11_absent + ay.grade_12_absent
# 		# ay.total_present = ay.grade_9_present + ay.grade_10_present + ay.grade_11_present + ay.grade_12_present
#
# 		# db.session.add(ay)
# 		# db.session.commit()
#
# # load_total_attendance()
# #name, math, reading, rating

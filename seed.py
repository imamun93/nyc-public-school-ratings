from sat_data import sat_data_list
from app import *
from ratings_data import ratings_list

import pdb
# creates the SATSchool and School models and tables in the database
db.create_all()

school_objects = []
sat_objects = []

def find_school_by_bn(bn):
	return db.session.query(School).filter(School.bn == bn).first()

def convert_rating(coded_rating):
	ratings= {'No Data': 0, 'U': 1, 'U ': 1, 'UD': 1, 'U/UD': 1, 'D': 2, 'P': 3, 'WD': 4, 'O':4, 'UPF': 1, '0': 0, 'DYO': 0, 'DY0': 0}
	return ratings[coded_rating.strip()]

for school in sat_data_list:
	if school['dbn']:
		bn = school['dbn'][2:6]
		new_school = School(dbn = school['dbn'], name = school['school_name'], bn = bn)
		school_objects.append(new_school)
		if school['test_takers'] != 's':
			new_satschool = SchoolSAT(dbn = school['dbn'], year = '2012', takers = int(school['test_takers']), reading_avg = int(school['reading_avg']), math_avg = int(school['math_avg']), writing_avg = int(school['writing_avg']))
			new_school.sats.append(new_satschool)
			sat_objects.append(new_satschool)

db.session.add_all(school_objects)
db.session.commit()
db.session.add_all(sat_objects)
db.session.commit()

for rating in ratings_list:
	rating_school = find_school_by_bn(rating['BN'])
	if rating_school: 
		#find school by bn
		year = int(rating['School_Year'][6:10])
		#get the year from the rating object 
		overall = convert_rating(rating['Overall_Rating'])
		new_rating = Rating(bn = rating['BN'], year = year, overall = overall )
		#associate rating with the school 
		new_rating.school = rating_school
		#let's get the core ratings and convert them with our helper method! 
		ic_1_1 = convert_rating(rating['Indicator_1.1'])
		# if rating['Indicator_1.2']:
		ic_1_2 = convert_rating(rating['Indicator_1.2'])
		ic_2_2 = convert_rating(rating['Indicator_2.2'])
		new_core = Core(ic_1_1 = ic_1_1, ic_1_2 = ic_1_2, ic_2_2 = ic_2_2)

		new_rating.core = new_core
		#convert culture subratings and create new culture object
		sc_3_4 = convert_rating(rating['Indicator_3.4'])
		sc_1_4 = convert_rating(rating['Indicator_1.4'])
		new_culture = Culture(sc_3_4 = sc_3_4, sc_1_4 = sc_1_4)
		#associate new_culture with the new rating 
		new_rating.culture = new_culture
		#gather improvement info 
		si_5_1 = convert_rating(rating['Indicator_5.1'])
		si_4_1 = convert_rating(rating['Indicator_4.1'])
		si_3_1 = convert_rating(rating['Indicator_3.1'])
		si_1_3 = convert_rating(rating['Indicator_1.3'])
		#create improvement object 
		new_improvement = Improvement(si_1_3 = si_1_3, si_3_1 = si_3_1, si_4_1 = si_4_1, si_5_1 = si_5_1)
		new_rating.improvement = new_improvement

		db.session.add_all([new_rating, new_core, new_culture, new_improvement]) 
		db.session.commit() 


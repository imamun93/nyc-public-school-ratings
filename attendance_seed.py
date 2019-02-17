from sat_data import sat_data_list
from app import *
from forest_data import forest_attendance_dict
# from school_year_att_data import school_year_att_list
import pdb

#create all the attendance_year_objects associate with school 

# key ('79X695', 2014, '12')
# values {'Present': 71, 'Absent': 28}

for key, values in forest_attendance_dict.items():
	current_school = School.query.filter(School.dbn == key[0]).first() 
	if current_school:
		current_year = key[1]
		dbn = current_school.dbn
		# pdb.set_trace()
		if not Attendance_Year.query.filter(Attendance_Year.school == current_school, Attendance_Year.year == current_year).first():
			new_att_year_object = Attendance_Year(dbn = dbn, year = current_year, roster = 0, total_absent = 0, total_present = 0)
			new_att_year_object.school = current_school
			# current_school.attendance_years.append(new_att_year_object)
			# db.session.refresh()
		else: 
			new_att_year_object = Attendance_Year.query.filter(Attendance_Year.school == current_school, Attendance_Year.year == current_year).first()
			# if Attendance_Year.query.filter(Attendance_Year.year == current_year):
		if key[2] == '09':
			new_att_year_object.grade_9_absent = values['Absent']
			new_att_year_object.grade_9_present = values['Present']
		elif key[2] == '10':
			new_att_year_object.grade_10_absent = values['Absent']
			new_att_year_object.grade_10_present = values['Present']
		elif key[2] == '11':
			new_att_year_object.grade_11_absent = values['Absent']
			new_att_year_object.grade_11_present = values['Present']
		elif key[2] == '12':
			new_att_year_object.grade_12_absent = values['Absent']
			new_att_year_object.grade_12_present = values['Present']
		else:
			continue

		db.session.add(new_att_year_object)
		db.session.commit() 

	# if current_school: 
	# 	year = int(attendance_y['SchoolYear'].strip())
	# 	print(current_school.name, year)
	# 	# pdb.set_trace()
	# 	roster = attendance_y['RosterCount']
	# 	dbn = attendance_y['School']
	# 	# current_school.attendance_years.append(Attendance_Year(dbn = dbn, year = year, roster = roster, total_absent = 0, total_present = 0))
	# 	new_att_year_object = Attendance_Year(dbn = dbn, year = year, roster = roster, total_absent = 0, total_present = 0)
	# 	print(new_att_year_object)
	# 	# current_school.attendance_years.append(new_att_year_object)
	# 	new_att_year_object.school= current_school
	# 	print("attendance years", current_school.attendance_years)
	# 	for grade_att in grade_9_list: 
	# 		if year == int(grade_att['SchoolYear'][-4:]):
	# 			rosters = grade_att['RosterCount']
	# 			absent = grade_att['Absent']
	# 			present = grade_att['Present']
	# 			new_grade_9= Grade_9( year = year, roster= rosters, absent= absent, present= present)
	# 			new_grade_9.attendance_year = new_att_year_object
	# 	for grade_att in grade_10_list: 
	# 		if year == int(grade_att['SchoolYear'][-4:]):
	# 			rosters = grade_att['RosterCount']
	# 			absent = grade_att['Absent']
	# 			present = grade_att['Present']
	# 			new_grade_10= Grade_10( year = year, roster= rosters, absent= absent, present= present)
	# 			new_grade_10.attendance_year = new_att_year_object
	# 	for grade_att in grade_11_list:
	# 		if year == int(grade_att['SchoolYear'][-4:]):
	# 			rosters= grade_att['RosterCount']
	# 			absent= grade_att['Absent']
	# 			present= grade_att['Present']
	# 			new_grade_11= Grade_11( year = year, roster=rosters, absent= absent, present= present)
	# 			new_grade_11.attendance_year = new_att_year_object
	# 	for grade_att in grade_12_list:
	# 		if year == int(grade_att['SchoolYear'][-4:]):
	# 			rosters= grade_att['RosterCount']
	# 			absent= grade_att['Absent']
	# 			present=grade_att['Present']
	# 			new_grade_12= Grade_12( year = year, roster= rosters, absent= absent, present= present)
	# 			new_grade_12.attendance_year = new_att_year_object
	# 	db.session.add(new_att_year_object)
	# 	db.session.commit() 


#year= db.Column(db.Integer, nullable= False)


#create each grade 
	#each grade needs to be associated with a 



# db.session.add_all(school_objects)
# db.session.commit()
# db.session.add_all(sat_objects)
# db.session.commit()




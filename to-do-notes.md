
Next Steps:
-----------


To Do:
------
- deal with null values. some don't have the same rating
- convert strings ratings to a number rating system
- make stuff into years



school
- id
- DBN NUmber
- Name
- Neighborhood (find neighborhood?)




sample sheet
https://infohub.nyced.org/docs/default-source/default-document-library/quality-review-report-template_18-192875b773f6114eec90de65dbe1b1d8c0.pdf




ratings 2005 - 2017
https://data.cityofnewyork.us/Education/2005-2017-School-Quality-Review-Ratings/9n9z-hh9p
-raw number
-percentage
- features of the scores - look at those and see if any correclation


- school_dbn
-has DBN with school name directly built in
https://data.cityofnewyork.us/Education/2018-19-Quality-Review-School-List/2rr4-rfvc


sat_scores
https://data.cityofnewyork.us/Education/2012-SAT-Results/f9bf-2cp4

SAT_ 2010 
https://data.cityofnewyork.us/Education/2010-SAT-College-Board-School-Level-Results/zt9s-n5aj


attendance 2012 - 2017
https://data.cityofnewyork.us/Education/2012-2017-Historical-Monthly-Grade-Level-Attendanc/wed3-5i35
- monthly
- yearly
- by school
- percentage of roster absence/preset
- and divided by grades (so we can do total, but have to aware of mixing middle and upper when talking about graduation rates)


graduation rate 2016-2017
https://data.cityofnewyork.us/Education/2016-2017-Graduation-Outcomes-School/nb39-jx2v


{'dbn': '01M292', 'school_name': 'HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES', 'test_takers': '29', 'reading_avg': '355', 'math_avg': '404', 'writing_avg': '363'}, {'dbn': '01M448', 'school_name': 'UNIVERSITY NEIGHBORHOOD HIGH SCHOOL', 'test_takers': '91', 'reading_avg': '383', 'math_avg': '423', 'writing_avg': '366'},
, overall_avg = int(school['math_avg']) + int(school['writing_avg']) + int(school['reading_avg'])



Range of possible values: 
U/UD, 
UPF, 
D, 
P, 
WD, 
O 

U/UD = Underdeveloped - 1
<!-- UPF = Underdeveloped with Proficient Features (only an option in 2007-8, 2008-9 and 2009-10) 1.5 -->
D = Developing 2
P = Proficient 3
WD = Well Developed 4 
<!-- O = Outstanding (only an option in 2007-8) 4.5 
 -->

ratings= {'No Data': 0, 'U': 1, 'U ': 1, 'UD': 1, 'U/UD': 1, 'D': 2, 'P': 3, 'WD': 4, 'O':4, 'UPF': 1, '0': 0, 'DYO': 0}

 {'BN': 'M307', 'School_Year': '06/01/2005 12:00:00 AM', 'Start_Date': '04/03/2006 12:00:00 AM', 'Overall_Rating': 'P', 'Indicator_1.1': 'P', 'Indicator_1.2': 'P', 'Indicator_1.3': 'P', 'Indicator_1.4': 'P', 'Indicator_1.5': 'No Data', 'Indicator_1.6': 'No Data', 'Indicator_1.7': 'No Data', 'IndicatorOverall_1': 'P', 'Indicator_2.1': 'WD', 'Indicator_2.2': 'WD', 'Indicator_2.3': 'WD', 'Indicator_2.4': 'WD', 'Indicator_2.5': 'WD', 'Indicator_2.6': 'No Data', 'Indicator_2.7': 'No Data', 'IndicatorOverall_2': 'WD', 'Indicator_3.1': 'WD', 'Indicator_3.2': 'WD', 'Indicator_3.3': 'WD', 'Indicator_3.4': 'WD', 'Indicator_3.5': 'WD', 'Indicator_3.6': 'WD', 'Indicator_3.7': 'WD', 'Indicator_3.8': 'WD', 'IndicatorOverall_3': 'WD', 'Indicator_4.1': 'WD', 'Indicator_4.2': 'WD', 'Indicator_4.3': 'WD', 'Indicator_4.4': 'WD', 'Indicator_4.5': 'WD', 'Indicator_4.6': 'WD', 'Indicator_4.7': 'WD', 'IndicatorOverall_4': 'WD', 'Indicator_5.1': 'P', 'Indicator_5.2': 'P', 'Indicator_5.3': 'P', 'Indicator_5.4': 'P', 'Indicator_5.5': 'No Data', 'Indicator_5.6': 'No Data', 'Indicator_5.7': 'No Data', 'IndicatorOverall_5': 'P'}


Note on school year. While some tables represent a school year as two years because it runs over two calendar years. 

Also, for attendance per school per year, we are doing an absent to present ratio. Higher the ratio, the more absent... absent:present ranges from lowest to highest 


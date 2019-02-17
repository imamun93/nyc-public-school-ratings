
from ratings_data import ratings_list 

bn_issues = {}

def find_bns(): 
	for school in ratings_list: 
		if len(school['BN']) != 4: 
			bn_issues['BN'] = school['BN']






sample = {'BN': 'M307', 'School_Year': '06/01/2005 12:00:00 AM', 'Start_Date': '04/03/2006 12:00:00 AM', 'Overall_Rating': 'P', 'Indicator_1.1': 'P', 'Indicator_1.2': 'P', 'Indicator_1.3': 'P', 'Indicator_1.4': 'P', 'Indicator_1.5': 'No Data', 'Indicator_1.6': 'No Data', 'Indicator_1.7': 'No Data', 'IndicatorOverall_1': 'P', 'Indicator_2.1': 'WD', 'Indicator_2.2': 'WD', 'Indicator_2.3': 'WD', 'Indicator_2.4': 'WD', 'Indicator_2.5': 'WD', 'Indicator_2.6': 'No Data', 'Indicator_2.7': 'No Data', 'IndicatorOverall_2': 'WD', 'Indicator_3.1': 'WD', 'Indicator_3.2': 'WD', 'Indicator_3.3': 'WD', 'Indicator_3.4': 'WD', 'Indicator_3.5': 'WD', 'Indicator_3.6': 'WD', 'Indicator_3.7': 'WD', 'Indicator_3.8': 'WD', 'IndicatorOverall_3': 'WD', 'Indicator_4.1': 'WD', 'Indicator_4.2': 'WD', 'Indicator_4.3': 'WD', 'Indicator_4.4': 'WD', 'Indicator_4.5': 'WD', 'Indicator_4.6': 'WD', 'Indicator_4.7': 'WD', 'IndicatorOverall_4': 'WD', 'Indicator_5.1': 'P', 'Indicator_5.2': 'P', 'Indicator_5.3': 'P', 'Indicator_5.4': 'P', 'Indicator_5.5': 'No Data', 'Indicator_5.6': 'No Data', 'Indicator_5.7': 'No Data', 'IndicatorOverall_5': 'P'}
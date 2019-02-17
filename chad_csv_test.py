

import pandas as pd 

# dct = pd.read_csv('school_ratings.csv', index_col=0, squeeze=True).to_dict()

dt = pd.read_csv('../data_store/2012_2017_school_attendance.csv').T.to_dict()
outer_limit = len(dt) - 1

# df = pd.read_csv("school_ratings.csv")
# read the date and close column and store as a list.
# time_list = list(df['date'])
# close_list = list(df['close'])
# perfect_dict = []
# # here take the minimum length
# # because avoiding index error
# take_length = min(len(time_list),len(close_list))
# for i in range(take_length):
#     temp_dict={}
#     temp_dict["Date"]=time_list[i]
#     temp_dict["Close"] = close_list[i]
#     perfect_dict.append(temp_dict)
# print(perfect_dict)
clean_dicts = []
for i in range(0, outer_limit): 
	new_dict = dt[i]
	clean_dicts.append(new_dict)

print(clean_dicts)

# ../data_store/2012_2017_school_attendance.csv 

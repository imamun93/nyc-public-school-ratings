import requests
r= requests.get('https://data.cityofnewyork.us/resource/734v-jeq5').json()
sat_scores= r
sat_scores


# sat_school1= sat_scores[0]
# sat_school1['test_takers']= sat_school1.pop('num_of_sat_test_takers')
# sat_school1['reading_avg']= sat_school1.pop('sat_critical_reading_avg_score')
# sat_school1['math_avg']= sat_school1.pop('sat_math_avg_score')
# del sat_school1['sat_writing_avg_score']

def sat_score():
    formatted_scores = []
    for sat_school1 in sat_scores:
        for key in sat_school1:
            if key == 'num_of_sat_test_takers':
                sat_school1['test_takers']= sat_school1.pop('num_of_sat_test_takers')
            if key == 'sat_critical_reading_avg_score':
                sat_school1['reading_avg']= sat_school1.pop('sat_critical_reading_avg_score')
            if key== 'sat_math_avg_score':
                sat_school1['math_avg']= sat_school1.pop('sat_math_avg_score')
            if key== 'sat_writing_avg_score':
                 sat_school1['writing_avg']= sat_school1.pop('sat_writing_avg_score')
        formatted_scores.append(sat_school1)
    return formatted_scores

print(sat_score())

# def sat_score():
#     counter=len(sat_scores)
    # while counter >=0:
#         for sat_school1 in sat_scores:
#             for key in sat_school1:
#                 if key == 'num_of_sat_test_takers':
#                     sat_school1['test_takers']= sat_school1.pop('num_of_sat_test_takers')
#                 if key == 'sat_critical_reading_avg_score':
#                     sat_school1['reading_avg']= sat_school1.pop('sat_critical_reading_avg_score')
#                 if key== 'sat_math_avg_score':
#                     sat_school1['math_avg']= sat_school1.pop('sat_math_avg_score')
#                 # if key== 'sat_writing_avg_score':
#                 #      del (sat_school1['sat_writing_avg_score'])
#         counter -=1
#     return sat_school1

# def scores():
#     total= len(sat_scores)
#     new_scores= []
#     while score < total:
#         for key in scores:
#             if key == 'num_of_sat_test_takers':
#                 score['test_takers']= score.pop('num_of_sat_test_takers')
#             if key == 'sat_critical_reading_avg_score':
#                 score['reading_avg']= score.pop('sat_critical_reading_avg_score')
#             if key== 'sat_math_avg_score':
#                 score['math_avg']= score.pop('sat_math_avg_score')
#             new_scores.append(score)
#         else:
#             break
#         return new_scores

from data_incubator import *

total = 0
total_people = 0

for index, row in data.iterrows():
    #print row['UGDS']
    #print row['SAT_AVG']
    if not pd.isnull(row['UGDS']) and not pd.isnull(row['SAT_AVG']):
        total = total + float(row['UGDS']) * float(row['SAT_AVG'])
        total_people += float(row['UGDS'])



print total/total_people

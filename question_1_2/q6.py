import pandas as pd


total_list = []

for i in xrange(2001,2011,1):

    total_num = 0
    total_percent = 0

    year = str(i+1)[-2:]
    datafile = "data/MERGED{}_{}_PP.csv".format(i,year)
    data = pd.DataFrame.from_csv(datafile)

    for index, row in data.iterrows():

        if not pd.isnull(row['UGDS_WOMEN']):
            try:
                percent = float(row['UGDS_WOMEN'])
            except ValueError:
                continue

            total_num += 1
            total_percent += percent

    total_list.append([total_num,total_percent])

total_count = sum([i[0] for i in total_list])
total_data = sum([i[1] for i in total_list])

res = total_data/total_count
print res

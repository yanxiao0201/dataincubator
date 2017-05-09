import pandas as pd

data = pd.DataFrame.from_csv("data/MERGED2014_15_PP.csv")

locale_list = [11,12,13,21,22,23,31,32,33,41,42,43]

local_city = {}
local_total = {}
for index, row in data.iterrows():

    if not pd.isnull(row['REGION']) and not pd.isnull(row['LOCALE']):
        try:
            region = int(row['REGION'])
            locale = int(row['LOCALE'])

        except ValueError:
            continue

        if region >= 0 and region <= 9 and locale in locale_list:
            local_total[region] = local_total.get(region,0) + 1

            if locale <= 13:
                local_city[region] = local_city.get(region,0) + 1

percent_list = []
for region in local_city:
    percent = float(local_city[region])/local_total[region]
    percent_list.append(percent)

#print percent_list
print max(percent_list)

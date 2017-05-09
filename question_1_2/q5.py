from data_incubator import *



mindiff = 100;
labels = ["UGDS_WHITE","UGDS_BLACK","UGDS_HISP","UGDS_ASIAN","UGDS_AIAN","UGDS_NHPI","UGDS_2MOR","UGDS_NRA","UGDS_UNKN","UGDS_WHITENH","UGDS_BLACKNH","UGDS_API"]
for index, row in data.iterrows():
    tmplist = []
    for label in labels:
        if not pd.isnull(row[label]):
            try:
                num = float(row[label])
            except ValueError:
                continue


            tmplist.append(num)

    if len(tmplist) > 1:
        diff = max(tmplist) - min(tmplist)
    elif len(tmplist) == 1:
        diff = tmplist[0]

    if sum(tmplist) > 0:
        mindiff = min(mindiff,diff)


print mindiff

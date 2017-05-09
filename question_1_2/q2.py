from data_incubator import *
import numpy as np
#data: dataframe

ave_score = []
enroll = []

for index, row in data.iterrows():
    #print row['UGDS']
    #print row['SAT_AVG']
    if not pd.isnull(row['ENRL_ORIG_YR2_RT']) and not pd.isnull(row['SAT_AVG']):
        try:
            num = float(row['ENRL_ORIG_YR2_RT'])
            ave_score.append(num)
        except ValueError:
            continue

        enroll.append(row['SAT_AVG'])


print np.corrcoef(ave_score,enroll)

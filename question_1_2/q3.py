from data_incubator import *
import numpy as np
from scipy import stats
import math

high_list = []
low_list = []

for index, row in data.iterrows():
    #print row['UGDS']
    #print row['SAT_AVG']

    if not pd.isnull(row['HI_INC_COMP_ORIG_YR4_RT']) and not pd.isnull(row['MD_INC_COMP_ORIG_YR4_RT']) and not pd.isnull(row['LO_INC_COMP_ORIG_YR4_RT']):
        try:
            high = float(row['HI_INC_COMP_ORIG_YR4_RT'])
            middle = float(row['MD_INC_COMP_ORIG_YR4_RT'])
            low = float(row['LO_INC_COMP_ORIG_YR4_RT'])
        except ValueError:
            continue

        high_list.append(high)
        low_list.append(low)

print np.mean(high_list) - np.mean(low_list)
#print len(high_list)
#print len(low_list)
twosample_results = stats.ttest_ind(high_list, low_list)
print np.log10(twosample_results[1])

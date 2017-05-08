from process_data import *
import sys

i = 7
filenames = []
for k in range(1,9):
    if k == i:
        continue
    filename = "PAMAP2_Dataset/Protocol/subject10{}.dat".format(k)
    filenames.append(filename)
data = DataProcessor()
data.load_train_data(filenames)

test_file = "PAMAP2_Dataset/Protocol/subject10{}.dat".format(i)
data.load_test_data(test_file)

data.RandomForest()
data.drawfigure1()
data.drawfigure2()

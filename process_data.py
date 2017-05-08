import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

class DataProcessor:
    def __init__(self):

        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.y_predict = None
        self.report = None
        self.importance = None
        self.res_dict = ['other','lying','sitting','standing','walking','running','cycling','Nordic walking',
                        'watching TV','computer work','car driving','ascending stairs','descending stairs','vacuum cleaning',
                        'ironing','folding laundary','house cleaning','playing soccer','rope jumping']

        self.feature_dict =[
 			'heart_rate',
 			'hand_temperature',
 			'hand_ac16g_1',
 			'hand_ac16g_2',
 			'hand_ac16g_3',
 			'hand_ac6g_1',
 			'hand_ac6g_2',
 			'hand_ac6g_3',
 			'hand_gyro_1',
 			'hand_gyro_2',
 			'hand_gyro_3',
 			'hand_magnet_1',
 			'hand_magnet_2',
 			'hand_magnet_3',
 			'hand_orien_1',
 			'hand_orien_2',
 			'hand_orien_3',
 			'hand_orien_4',
 			'chest_temperature',
 			'chest_ac16g_1',
 			'chest_ac16g_2',
 			'chest_ac16g_3',
 			'chest_ac6g_1',
 			'chest_ac6g_2',
 			'chest_ac6g_3',
 			'chest_gyro_1',
 			'chest_gyro_2',
 			'chest_gyro_3',
 			'chest_magnet_1',
 			'chest_magnet_2',
 			'chest_magnet_3',
 			'chest_orien_1',
 			'chest_orien_2',
 			'chest_orien_3',
 			'chest_orien_4',
 			'ankle_temperature',
 			'ankle_ac16g_1',
 			'ankle_ac16g_2',
 			'ankle_ac16g_3',
 			'ankle_ac6g_1',
 			'ankle_ac6g_2',
 			'ankle_ac6g_3',
 			'ankle_gyro_1',
 			'ankle_gyro_2',
 			'ankle_gyro_3',
 			'ankle_magnet_1',
 			'ankle_magnet_2',
 			'ankle_magnet_3',
 			'ankle_orien_1',
 			'ankle_orien_2',
 			'ankle_orien_3',
 			'ankle_orien_4']


    def load_train_data(self,filenames):

        total_data = []
        total_res = []

        for filename in filenames:
            data, res = self.process_single_file(filename)

            total_data += data
            total_res += res

        self.X_train = np.asarray(total_data)
        self.y_train = total_res

    def process_single_file(self,filename):

        tmplist = []
        data = []
        res = []

        datafile = open(filename,'r')


        for line in datafile:
            items = line.split()

            if int(items[1]) == 0:
                continue

            if items[2] != 'NaN':

                for i in range(2,len(items)):
                    if items[i] == 'NaN':
                        tmplist = []
                        break
                    else:
                        tmplist.append(float(items[i]))

                if tmplist != []:
                    res.append(int(items[1]))
                    data.append(tmplist)
                    tmplist = []

        print "Processing file {}".format(filename)

        datafile.close()
        return data, res


    def load_test_data(self,filename):
        data, res = self.process_single_file(filename)
        self.X_test = np.asarray(data)
        self.y_test = res


    def RandomForest(self):
        print "Random Forest Classifer..."

        rfc = RandomForestClassifier(n_estimators = 28, random_state =0)

        rfc.fit(self.X_train,self.y_train)

        self.y_predict = rfc.predict(self.X_test)
        print "The mean accuracy is {}".format(rfc.score(self.X_test,self.y_test))

        print "confusion matrix"
        print confusion_matrix(self.y_test,self.y_predict)

        print "classification report"
        self.report = classification_report(self.y_test,self.y_predict)

        print self.report

        self.importance = rfc.feature_importances_


    def drawfigure1(self):
        rawreport = self.report.split()[4:-7]

        group = []
        precision = []

        for i in xrange(0,len(rawreport),5):
            idx = int(rawreport[i])
            group.append(self.res_dict[idx])
            precision.append(float(rawreport[i+1]))

        y_pos = np.arange(len(group))

        plt.figure('Precision')
        plt.barh(y_pos,precision,align = 'center',alpha=0.5)
        plt.yticks(y_pos,group)
        plt.xlabel('Precision')
        plt.title('Precision of Activity Prediction')

        plt.savefig('Precision.png',bbox_inches='tight')


    def drawfigure2(self):

        y_pos = np.arange(len(self.importance))

        y_label = []
        for y in y_pos:
            y_label.append(str(y))

        plt.figure('Importance')
        plt.barh(y_pos,self.importance,align = 'center')
        plt.ylim([-5,55])

        plt.xlabel('Importance')
        plt.title('Importance of the Features')

        plt.savefig('Importance')

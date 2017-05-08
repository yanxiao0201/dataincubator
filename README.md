# dataincubator
This is the source code for the data incubator challenge summer 2017


##Proposal

Personal Lifestyle Recommendation System 

A healthy lifestyle is closely associated to individual success and long life. A precise, but individually optimized personal lifestyle tracking and recommendation system will have great market potential. Traditional methods involve long-time tracking of clients’ daily life pattern and consultation of health consultants. These methods are not only expensive, but also have high variance, due to the experience level of different health consultants, as well as the loss of continuous data from the clients. 

In this project, I am proposing to use a combination of physical activity monitoring units, and machine learning algorithm to develop a completely personalized lifestyle recommendation system. Basically these monitoring units will collect real-time data from user continuously, and a trained classifier will predict the activity based on the data, and record the length of each activity. At the end of the day, the system can give recommendations to the user. For example, if the system detect that the user is doing computer work for a long time, it will alert the user to exercise more. The user can also input more personal life data, if they want to increase the accuracy of the system. There is no upper limit for the capability of this system. 

The essential piece for this project is to develop a classification system, based on machine learning algorithms, that can accurately determine the user’s activity based on the monitor data. To prove the feasibility of the project, I used the PAMAP2_Dataset online, that have monitoring information from 9 healthy individuals. These data include timestamp, activityID, heart rate, temperature, and positioning information from 3 different monitors.  Using these data as features, I tried to train a classifier with Random Forest, Support Vector Machine and Neuron Network algorithms. Eventually I decide to use Random Forest after the tuning of the parameters. As shown in figure “Precision of Activity Prediction”, my classification algorithm can accurately determine the majority of the activities. It reaches >90% precision when detecting activities such as “playing soccer”, or “housing cleaning”, “cycling”, “running”, and in general have very high precision rate. Overall I can reach >87% accuracy for all the data tested. 

In order to improve the accuracy rate of the system, I performed analysis on the significance of all the features I have been feeding the classifier. Base on the figure “Importance of the Features”, some of the features contribute significantly while some other features are less importance in the classification process. 
The y-axis labels are the number code for each feature because there are ~60 features in the data.  For example, No.0 feature, the body temperature, was shown to be more important, and certain velocity information from some specific monitor has shown to be key in identifying certain movements. With more data and potential funding support, I can optimize the algorithm to further increase the performance of the system. 

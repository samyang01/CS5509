import numpy as np
from numpy import genfromtxt
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
from sklearn import metrics

# I chose to use the wine quality dataset from UCI
# Using genfromtxt to read the csv file into numpy array object wines
wines=genfromtxt("winequality-red.csv", delimiter=';', skip_header=1)

# Next, index the array into features and targets
num=len(wines)
wine_features=np.array(wines[0:,0:-1])
wine_quality=wines[0:,-1]

# Next we instantiate the Linear Discriminant Analysis method
LDA=LinearDiscriminantAnalysis()

# Next we split the wine dataset into a testing and training portion using train_test_split
x_train, x_test, y_train, y_test = train_test_split(
wine_features, wine_quality, test_size=0.6, train_size=0.4)

# Next we fit the training data to the LDA method
predictor=LDA.fit(x_train, y_train)

# Next we use cross_val_predict on the test data set with the fitted LDA algorithm
# and use metrics.accuracy_score to give us a score of correct predictions
predicted = cross_val_predict(predictor, x_test, y_test)
print('Result: ', metrics.accuracy_score(y_test,predicted))

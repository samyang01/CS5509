# Choose one of the dataset using the datasets features in the scikit-learn
# 2)Load the dataset
# 3)According to your dataset, split the data to 20% testing data, 80% training data
# 4)Apply SVC with Linear kernel
# 5)Apply SVC with RBF kernel
# 6)Report the accuracy of the model on both models separately and report their differences
# 7)Report your view how can you increase the accuracy and which kernel is the best for your dataset and why

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import cross_val_predict
from sklearn import metrics

# for this project, I chose the digits dataset that comes with Sklearn
# the dataset is conveniently split into features(images) and targets already
digits=datasets.load_digits()

# First, we reshape the data of the images into a array that will be accepted by the classifier,
# essentially turning it into a column vector
num = len(digits.images)
data = digits.images.reshape((num, -1))

# Next, we split the data into a training set and testing set using train_test_split
x_train, x_test, y_train, y_test = train_test_split(
data, digits.target, train_size=0.4, test_size=0.6)

# Next we instantiate 2 SVM classifiers, one using a linear kernel, the other using a 'rbf' or radial basis function
# kernel in order to compare the difference
classifier1=svm.SVC(kernel='linear')
classifier1.fit(x_train,y_train)

classifier2=svm.SVC(kernel='rbf')
classifier2.fit(x_train, y_train)

# Next we test the 2 classifiers with the testing set using cross_val_predict and output the accuracy score using
# metrics.accuracy_score
predicted1 = cross_val_predict(classifier1,x_test, y_test)
predicted2 = cross_val_predict(classifier2,x_test, y_test)
print('Result Linear: ', metrics.accuracy_score(y_test, predicted1))
print('Results RBF: ', metrics.accuracy_score(y_test, predicted2))

''' Notes: The Linear SVM classifier is much more accurate compared to the RBF SVM classifier, the reason for this
is because the RBF is over-fitting the training data, making the model not very generalizable, or in other
words, increasing the variance of the model '''
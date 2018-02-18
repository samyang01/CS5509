# T shirt problem

# import data into pandas table
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# scrapped the data for this project from the following website that contains an HTML table of
# height and weight for 2500 individuals, only the first 500 are used to speed up the processing

# read in the table as a list of panda dataframes
htwt_list=pd.read_html("http://socr.ucla.edu/docs/resources/SOCR_Data/SOCR_Data_Dinov_020108_HeightsWeights.html")
# there is only 1 table on the given page so we select the index 0 dataframe
htwt_table=htwt_list[0]

# store the first and second column as a series in x and y respectively, x stores the weight in inches and y stores
# the weight in pounds

x=htwt_table.iloc[1:500,1]
y=htwt_table.iloc[1:500,2]

# create an empty nested array of 2 values
z=np.zeros((499,2))

# populate the array with x,y values
for i in range(len(x)):
    z[i][0]=x.iloc[i]
    z[i][1]=y.iloc[i]

# instantiate Kmean with 4 clusters (small, medium, large, extra large)
kmeans=KMeans(n_clusters=4)

# fit the data stored in z with the kmeans.fit method
kmeans.fit(z)

# pull centroids and labels information from Kmeans on z
centroids=kmeans.cluster_centers_
labels=kmeans.labels_

colors = ['g.','r.','c.','y.','b.']

#plot the individual data points based on the label assigned by Kmeans
for i in range(len(z)):
    plt.plot(z[i][0], z[i][1], colors[labels[i]], markersize = 10)

#plot the centroids
plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()

#References
#https://pythonprogramming.net/flat-clustering-machine-learning-python-scikit-learn/
#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html
#https://www.dataquest.io/blog/pandas-python-tutorial/
#http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans

# Nearest neighbour and K-means clustering algorithm

Nearest Neighbour :  
The program reads red, blue and unknown data points from a ".txt" file.  
Parse them into list[list[list]].  
Compare the unknown data points with red and blue datasets.  
Based on their distance, classify the unknown dataset into either blue or red and saves the output as a text file.  
  
![Nearest Neighbour Classifier Example](https://github.com/Adnan525/nearestneighbourandkmeans/blob/master/nearestNeighbourExample.PNG?raw=true)  
  
K-means Clustering :  
The algorithm reads point from a text data file as usual.
Converts the points into list[list[list]].  
Select K number of data points from the dataset randomly (Have to be unique).  
Use the random points as cluster centers and compare against all the points in the dataset.  
Based on their distance, assigns the points into K number of clusters and stores in a python dictionary where:  
&emsp;1) KEYS of the dictionary are index values like 0,1,2,3... which will correspond to list returned from mydict.keys()  
&emsp;2) The points of a same cluster are all stored in a list and added to the dictionary as a value to their respective cluster.  
The kMeans() recursive function keeps generating cluster and center points until the difference between old and new center points is less than threshold (0.5).  
The function will return a dictionary, we will generate center points again using the genAverageCenterPoints() function and plot the data using tkInter.  
  
![K-Means Example](https://github.com/Adnan525/nearestneighbourandkmeans/blob/master/kmeans.PNG?raw=true)  


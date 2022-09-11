# function to calculate distance
# point 1 and point 2 will be lists
import math


def calculate_distance(point1, point2):
    distance = 0
    # both points will have same length
    for i in range(len(point1)):
        distance += (point2[i] - point1[i]) ** 2
    distance = math.sqrt(distance)
    return distance



###function to find the cluster
def find_cluster(point, centroids):
    clusture = []
    return clusture

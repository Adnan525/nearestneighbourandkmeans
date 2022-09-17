import utility


# returns a dictionary where
#   keys = center points
#   values = list of points that belong to the center point
def genCluster(dataset, center):
    cluster = []
    d = {}
    for i in range(0, len(center)):
        d[i] = []

    belongingCluster = None
    leastDistance = None
    for point in dataset:
        for c in center:
            dist = utility.calculate_distance(point, c)
            if leastDistance is None or leastDistance > dist:
                leastDistance = dist
                belongingCluster = center.index(c)
        d[belongingCluster].append(point)
        belongingCluster = None
        leastDistance = None

    return d


# returns the average points of k number of clusters as a list[list[float]]
def genAvgCenter(clusterDict):
    allKeys = clusterDict.keys()
    # point dimension
    dim = len(clusterDict[0][0])
    result = []

    for key in allKeys:
        avCenter = []
        temp = clusterDict[key]
        for i in range(0, dim):
            su = 0
            for point in temp:
                su = su + point[i]
            su = su / len(temp)
            avCenter.append(su)
        result.append(avCenter)
    return result


# takes a old = list[list[float]] and new = list[list[float]] and threshold = int
# returns false or true
def genNewClusterCenter(old: list[list[float]], new: list[list[float]], threshold: int):
    isChangeNecessary = False
    for i in range(0, len(old)):
        for j in range(0, len(old[i])):
            if utility.dummyAbs(old[i][j] - new[i][j]) > utility.dummyAbs(threshold):
                isChangeNecessary = True
                break
    return isChangeNecessary

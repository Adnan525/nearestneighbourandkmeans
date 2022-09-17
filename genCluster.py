import utility


def genCluster(dataset, center):
    cluster = []
    d = {}
    for i in range(0,len(center)):
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

def getAverageCluster(centerPoints: list[list[float]], di):
    allKeys = di.keys()
    for key in allKeys:
        # list[list[float]]
        temp = di[key]
        valX = 0
        valY = 0
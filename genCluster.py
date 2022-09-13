import utility


def genCluster(dataset: list[list[float]], center: list[list[float]]):
    cluster = []
    belongingCluster = None
    leastDistance = None
    for point in dataset:
        for c in center:
            dist = utility.calculate_distance(point, c)
            if leastDistance is None or leastDistance > dist:
                leastDistance = dist
                belongingCluster = center.index(c)
        cluster.append(belongingCluster)
        belongingCluster = None
        leastDistance = None

    return cluster

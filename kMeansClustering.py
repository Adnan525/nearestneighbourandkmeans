import genClusterCenter as genClusCent
import genCluster
import clustering as cluster


def kMeans(read_data: list[list[float]], threshold: float, clusterCenterList: list[list[float]]):

    getCluster = genCluster.genCluster(read_data, clusterCenterList)
    newCenter = genCluster.genAvgCenter(getCluster)
    isNewCenterNecessary = genCluster.genNewClusterCenter(clusterCenterList, newCenter, threshold)
    if isNewCenterNecessary:
        kMeans(read_data, threshold, newCenter)
    else:
        return getCluster

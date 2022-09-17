import genCluster
import io_module as io
import makeCoordinates as coord
import genClusterCenter as genClusCent
import clustering as cluster
import kMeansClustering
import render

# Reading the Red, blue and unknown valude form the text file
data_2c_2d = "datasets/data_2c_2d.txt"
data_4c_2d = "datasets/data_4c_2d.txt"
data_2c_4d = "datasets/data_2c_4d.txt"
data_4c_4d = "datasets/data_4c_4d.txt"

read_data = io.read_multi_dim_data(data_4c_2d)
read_data = coord.genCoord(read_data)

# Any number greater than 1
cluster_size = int(input("Input the cluster size:"))

#setup
# find the Dimension and Data sample here
num_of_dimension = len(read_data[0])
sample_size = len(read_data)
threshold = 0.5

# Create a random cluster center based on number of dimension(num_of_dimension) and size of cluster(
# select_cluster_size) returns the index value from the main dataset length
cluster_center = cluster.generate_K_cluster_centres(cluster_size, sample_size)

# create list based on the cluster center
clusterCenterList = genClusCent.genCenter(cluster_center, read_data)

if __name__ == "__main__":
    kmc = kMeansClustering.kMeans(read_data, threshold, clusterCenterList)
    finalCenterPoints = genCluster.genAvgCenter(kmc)
    print(finalCenterPoints)
    render.renderClusters(kmc, finalCenterPoints)
    render.run_tk_window()

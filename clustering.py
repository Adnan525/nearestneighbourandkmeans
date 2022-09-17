# module to handle clustering
# method available generate_K_cluster_centers, calculate_all_distances, find_shortest_distance, calculate_memberships, calculate_sum_2, calculate_cluster_centres
import utility


def calculate_distance(point1, point2):
    distance = 0
    # both points will have same length
    for i in range(len(point1)):
        distance += (point2[i] - point1[i]) ** 2
    distance = distance ** 0.5
    return distance


# function to find cluster center
def calculate_cluster_center():
    cluster_center = None
    return cluster_center


# generate cluster centers with K
def generate_K_cluster_centres(kSize, datasetSize):
    cluster_center_list = []
    seed = datasetSize
    while len(cluster_center_list)<kSize:
        temp = utility.customRandom(seed, 0, datasetSize, 10**12, True)
        if cluster_center_list.count(temp) <= 0:
            cluster_center_list.append(temp)
            seed -= 1
    # cluster_center_list = random.sample(range(0, datasetSize), kSize)

    return cluster_center_list

# function to calculate distance
# point 1 and point 2 will be lists
def calculate_distance(point1, point2):
    distance = 0
    # both points will have same length
    for i in range(len(point1)):
        distance += (point2[i] - point1[i]) ** 2
    distance = distance ** 0.5
    return distance


# function to find the cluster
def find_cluster(point, centroids):
    clusture = []
    return clusture


def dummyAbs(i: float):
    return i if i > 0 else i * -1


# The function is collected from stackoverflow, author : user2008484
# https://stackoverflow.com/questions/22950768/random-int-without-importing-random
def customRandom(seed=None, a=0, b=10, N=10 ** 12, integer=True):
    '''Pass a seed to generate new sequence, otherwise next value is returned.'''
    if seed:
        global _rand_generator
        if integer:
            hash_plus = lambda j: int(
                a + (b - a) * (abs(hash(str(hash(str(seed) + str(j + 1))))) % 10 ** 13) / 10 ** 13)
        else:
            hash_plus = lambda j: a + (b - a) * (abs(hash(str(hash(str(seed) + str(j + 1))))) % 10 ** 13) / 10 ** 13
        _rand_generator = (hash_plus(j) for j in range(N))
    try:
        return next(_rand_generator)
    except:
        print("Random seed required.")

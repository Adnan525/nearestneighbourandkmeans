def genCenter(ranCen, dataset):
    clusterCenterList = []
    for index in ranCen:
        clusterCenterList.append(dataset[index])
    return clusterCenterList
def genCenter(ranCen: list[int], dataset: list[list[float]]):
    clusterCenterList = []
    for index in ranCen:
        clusterCenterList.append(dataset[index])
    return clusterCenterList
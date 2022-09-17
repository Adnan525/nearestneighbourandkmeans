# Function to read multi-dimension data from a file

def read_multi_dim_data(filename):
    """
    Reads a multi-dimensional data from a file.
    """
    dataset = []
    with open(filename, "r") as f:
        for line in f:
            dataset.append(line)

    return dataset


def writeToFile(targetUnknown: list[list[float]], classified: list[str], dimension: int):
    filename = 'output/output_' + str(dimension) + 'D.txt'
    f = open(filename, 'w')
    for i in range(0, len(classified)):
        temp = str(targetUnknown[i])
        f.write(f"({temp[1:len(temp) - 1]}) {classified[i]}\n")
        print(f'The unknown point ({temp[1:len(temp) - 1]}) falls in {classified[i]} class')

    f.close()
    print(f"=============output stored in {filename}=============")

# the function will accept a list and return a list of lists as coordinates
# will convert string to float values

def genCoord(li: list[str]):
    coordinates = []
    for line in li:
        # get rid of the new line char
        # last line won't have the \n character
        targetLine = line[0:len(line)] if line == li[len(li)-1] else line[0:len(line)-1]
        tempString = targetLine.split(" ")
        tempList = []
        for val in tempString:
            co = float(val)
            tempList.append(co)
        coordinates.append(tempList)
    return coordinates

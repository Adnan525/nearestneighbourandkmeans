import utility
def findNeighbour(red : list[list[float]], blue : list[list[float]], unknown : list[list[float]]):
    shortestRed = None
    shortestBlue = None
    result = []

    for un in unknown:
        for r in red:
             dist = utility.calculate_distance(un, r)
             if shortestRed is None or shortestRed > dist :
                 shortestRed = dist
        for b in blue:
            dist = utility.calculate_distance(un, b)
            if shortestBlue is None or shortestBlue > dist:
                shortestBlue = dist
        result.append("red" if shortestRed < shortestBlue else "blue")
        shortestRed = None
        shortestBlue = None
    return result
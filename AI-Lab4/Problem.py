class Problem:
    countries = {}
    neighbors = {}
    colors = {}

    def __init__(self, filename):
        f = open(filename, "r")
        countriestxt = f.readline()
        countriestxt = countriestxt.replace(" ", "")
        countriestxt = countriestxt.replace("\n", "")
        countries = countriestxt.split(",")

        neighborstxt = f.readline()
        neighborstxt = neighborstxt.replace(" ", "")
        neighborstxt = neighborstxt.replace("\n", "")
        neighborsTemp = neighborstxt.split(";")
        for s in neighborsTemp:
            temp = s.split(":")
            temp[1] = temp[1].replace("{", "")
            temp[1] = temp[1].replace("}", "")
            Problem.neighbors[temp[0]] = temp[1].split(",")

        colorstxt = f.readline()
        colorstxt = colorstxt.replace(" ", "")
        colorstxt = colorstxt.replace("\n", "")
        colorsTemp = colorstxt.split(";")
        for s in colorsTemp:
            temp = s.split(":")
            temp[1] = temp[1].replace("{", "")
            temp[1] = temp[1].replace("}", "")
            Problem.colors[temp[0]] = temp[1].split(",")

        print(countries)
        print(Problem.neighbors)
        print(Problem.colors)

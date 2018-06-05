def contrast(matrix):
    height, width = matrix.shape
    sumContrast = 0

    for i in range(height):
        for j in range(width):
            sumContrast += ((abs(i - j))**2) * matrix[i, j]
    return sumContrast

def energy(matrix):
    height, width = matrix.shape
    sumEnergy = 0

    for i in range(height):
        for j in range(width):
            sumEnergy += (matrix[i, j])**2
    return sumEnergy

def homogeneity(matrix):
    height, width = matrix.shape
    sumHomogeneity = 0

    for i in range(height):
        for j in range(width):
            sumHomogeneity += matrix[i, j]/(1 + (abs(i - j)))
    return sumHomogeneity

def correlation(matrix):
    height, width = matrix.shape
    listSumI = []
    listSumJ = []
    sumJ = 0
    sumI = 0
    standardDeviationJ = 0

    for i, y in zip(range(height), range(width)):
        for j, x in zip(range(width), range(height)):
            sumI += matrix[i, j]
            sumJ += matrix[x, y]
        listSumI.append(sumI)
        listSumJ.append(sumJ)

    # print(len(listSumI) == height)
    # print(len(listSumJ) == width)

    averageSumI = 0
    averageSumJ = 0

    for i in range(height):
        averageSumI += i * (listSumI[i])
    for j in range(width):
        averageSumJ += j * (listSumJ[j])

    sumAux = 0
    for i in range(height):
        sumAux += ((i - averageSumI)**2) * listSumI[i]
    standardDeviationI = sumAux**(1/2)
    sumAux = 0
    for j in range(width):
        sumAux += ((j - averageSumJ)**2) * listSumJ[j]
    standardDeviationJ = sumAux**(1/2)

    sumCorrelation = 0
    for i in range(height):
        for j in range(width):
            sumCorrelation += ((i - averageSumI) * (j - averageSumJ) * matrix[i, j])/\
                              (standardDeviationI * standardDeviationJ)
    return sumCorrelation



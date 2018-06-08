import numpy as np

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

    for i, j in zip(range(height), range(width)):
        sumI = np.sum(matrix[i, :])
        sumJ = np.sum(matrix[:, j])
        listSumI.append(sumI)
        listSumJ.append(sumJ)
        sumI = 0
        sumJ = 0

    averageSumI = 0
    averageSumJ = 0

    for i in range(1, height+1):
        averageSumI += i * (listSumI[i-1])
    for j in range(1, width+1):
        averageSumJ += j * (listSumJ[j-1])

    sumAux = 0
    for i in range(1, height+1):
        sumAux += ((i - averageSumI)**2) * listSumI[i - 1]
    standardDeviationI = sumAux**(1/2)
    sumAux = 0
    for j in range(1, width+1):
        sumAux += ((j - averageSumJ)**2) * listSumJ[j - 1]
    standardDeviationJ = sumAux**(1/2)

    sumCorrelation = 0
    for i in range(1, height+1):
        for j in range(1, width+1):
            sumCorrelation += ((i - averageSumI) * (j - averageSumJ) * matrix[i-1, j-1])/\
                              (standardDeviationI * standardDeviationJ)
    return sumCorrelation

def allFeatures(matrix, exclude = 0):
    height, width = matrix.shape
    sumContrast = 0
    sumCorrelation = 0
    sumEnergy = 0
    sumHomogeneity = 0
    listSumI = []
    listSumJ = []

    for i, j in zip(range(height), range(width)):
        sumI = np.sum(matrix[i, :])
        sumJ = np.sum(matrix[:, j])
        listSumI.append(sumI)
        listSumJ.append(sumJ)

    averageSumI = 0
    averageSumJ = 0
    if exclude != 4:
        for i in range(1, height + 1):
            averageSumI += i * (listSumI[i - 1])
        for j in range(1, width + 1):
            averageSumJ += j * (listSumJ[j - 1])

        sumAux = 0
        for i in range(1, height + 1):
            sumAux += ((i - averageSumI) ** 2) * listSumI[i - 1]
        standardDeviationI = sumAux ** (1 / 2)
        sumAux = 0
        for j in range(1, width + 1):
            sumAux += ((j - averageSumJ) ** 2) * listSumJ[j - 1]
        standardDeviationJ = sumAux ** (1 / 2)

    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if exclude != 1:
                sumContrast += ((abs(i - j))**2) * matrix[i - 1, j - 1]
            if exclude != 2:
                sumEnergy += (matrix[i - 1, j - 1])**2
            if exclude != 3:
                sumHomogeneity += matrix[i - 1, j - 1]/(1 + (abs(i - j)))
            if exclude != 4:
                sumCorrelation += ((i - averageSumI) * (j - averageSumJ) * matrix[i - 1, j - 1]) / \
                                  (standardDeviationI * standardDeviationJ)

    return [sumContrast, sumCorrelation, sumEnergy, sumHomogeneity]

def featuresWriter(imageNumber,contrast, correlation, energy, homogeneity):
    if imageNumber + 1 > 25 and imageNumber + 1 <= 50:
        T = "D2"
    elif imageNumber + 1 > 50:
        T = "G3"
    else:
        T = "A1"

    b = "   "
    featuresFile = open("featuresFile.txt", "a")
    featuresFile.write(str(imageNumber + 1) + b + str(contrast) + b + str(correlation)
                       + b + str(energy) + b + str(homogeneity) + b + T + "\n")
    featuresFile.close()

import numpy as np

trainFeaturesArray = [[4.07322962e+02, 8.66683290e-01, 1.76446580e-04, 1.82157475e-01],
 [1.71112046e+02, 9.32020007e-01, 3.98442505e-04, 2.64235503e-01],
 [6.20499619e+01, 9.81776961e-01, 1.23903365e-03, 3.41201375e-01]]

trainFeaturesArray = np.array(trainFeaturesArray, dtype = np.float64)

testFeaturesArray = [[6.38044560e+01, 9.80553496e-01, 4.97879166e-04, 0.00000000e+00],
 [3.62183390e+02, 8.37951381e-01, 2.25757036e-04, 0.00000000e+00],
 [3.02827137e+02, 8.25157130e-01, 2.16338249e-04, 0.00000000e+00]]

testFeaturesArray = np.array(testFeaturesArray, dtype = np.float64)

auxList = []
confusionMatrix = np.array((
               [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]), dtype= np.uint8)

height, width = testFeaturesArray.shape
print(height, width)
for i in range(height):
    resultFeaturesArray = (trainFeaturesArray - testFeaturesArray[i, :])**2
    print(resultFeaturesArray)
    if height < 1:
        flag = 0
    elif height > 1 and height < 3:
        flag = 1
    else:
        flag = 2
    for j in range(height):
        distance = (np.sum(resultFeaturesArray[j, :3]))**(1/2)
        auxList.append(distance)
    print(auxList)
    distanceAsphalt = auxList[:1]
    print("DA:", distanceAsphalt)
    distanceDanger = auxList[1:2]
    distanceGrass = auxList[2:]
    print("DG:", distanceGrass)
    distanceAsphalt.sort()
    distanceDanger.sort()
    distanceGrass.sort()
    asphaltCounter = 0
    dangerCounter = 0
    grassCounter = 0
    for counter in range(1):
        auxList = [(distanceAsphalt[counter], 1), (distanceDanger[counter], 2), (distanceGrass[counter], 3)]
        auxList.sort()
        if auxList[0][1] == 1:
            asphaltCounter += 1
        elif auxList[0][1] == 2:
            dangerCounter += 1
        else:
            grassCounter += 1
    auxList = [(asphaltCounter, 0), (dangerCounter, 1), (grassCounter, 2)]
    auxList.sort()
    confusionMatrix[auxList[0][1], flag] += 1
    auxList = []

print(confusionMatrix)
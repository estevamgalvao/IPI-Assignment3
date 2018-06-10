import cv2
import numpy as np
from functions.rgb_greyscale import RGB2Greyscale

img = cv2.imread("/home/estevamgalvao/Documentos/PycharmProjects/IPI-Assignment3/images/t.tif")
cv2.imshow('T', img)
cv2.waitKey(0)

img = RGB2Greyscale(img)

height, width = img.shape
print(height, width)
print("Sum Total: ", np.sum(img))

for i, j in zip(range(height), range(width)):
    print(np.sum(img[i, :]))
    print(np.sum(img[:, j]))
for j in range(width):
    pass
    # print(img[i, j, 0])



    #
    # # featuresWriter(k, features[0], features[1], features[2], features[3])
    #
    # file = open("featuresFile.txt", "r")
    # auxArray = file.readlines()
    # print(auxArray)
    # featuresArray = []
    #
    # for feature in auxArray:
    #     feature = feature.split()
    #     featuresArray.append(feature)
    # print(featuresArray)
    # for glcm in featuresArray:
    #     print(glcm)
    #     print()
    #     for feature in glcm:
    #         print(feature)

matrixGLCM = np.array((
    [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 9, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]), dtype= np.float64)
confusionMatrix = np.array((
               [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]), dtype= np.uint8)

#matriz glcm
#featureExtraction
#corelação e anular alguma característica
#plotar as 3 característcas restantes
#calcular centro de massa
#testar as outras 25 imagens
#criar matriz de confusão



# Asphalt -> anular Correlação
# Danger -> anular Contraste
# Grass -> anular Correlação

# # ASFALTO E GRAMA #
# plt.scatter(featuresArray[:26, 0], featuresArray[:26, 2], color='blue')
# plt.scatter(featuresArray[:26, 0], featuresArray[:26, 3], color='red')
# plt.scatter(featuresArray[:26, 2], featuresArray[:26, 3], color='green')
# plt.xlabel('Contrast')
# plt.ylabel('')
#
# plt.scatter(featuresArray[51:, 0], featuresArray[51:, 2], color='blue')
# plt.scatter(featuresArray[51:, 0], featuresArray[51:, 3], color='red')
# plt.scatter(featuresArray[51:, 2], featuresArray[51:, 3], color='green')
#
# # PERIGO #
# plt.scatter(featuresArray[26:51, 1], featuresArray[26:51, 2], color='blue')
# plt.scatter(featuresArray[26:51, 1], featuresArray[26:51, 3], color='red')
# plt.scatter(featuresArray[26:51, 2], featuresArray[26:51, 3], color='green')


# # ASFALTO E GRAMA #
# plt.scatter(featuresArray[:26, 0], featuresArray[:26, 2], color='blue')
# plt.scatter(featuresArray[51:, 0], featuresArray[51:, 2], color='red')
# plt.xlabel('Contrast')
# plt.ylabel('Energy')
# plt.savefig("./CONvsENE.png")
# plt.close()
#
# plt.scatter(featuresArray[:26, 0], featuresArray[:26, 3], color='yellow')
# plt.scatter(featuresArray[51:, 0], featuresArray[51:, 3], color='purple')
# plt.xlabel('Contrast')
# plt.ylabel('Homogeneity')
# plt.savefig("./CONvsHOM.png")
# plt.close()
#
# # TODOS #
# plt.scatter(featuresArray[:26, 2], featuresArray[:26, 3], color='orange')
# plt.scatter(featuresArray[51:, 2], featuresArray[51:, 3], color='green')
# plt.scatter(featuresArray[26:51, 2], featuresArray[26:51, 3], color='brown')
# plt.xlabel('Energy')
# plt.ylabel('Homogeneity')
# plt.savefig("./ENEvsHOM.png")
# plt.close()
#
#
# # PERIGO #
# plt.scatter(featuresArray[26:51, 1], featuresArray[26:51, 2], color='black')
# plt.xlabel('Correlation')
# plt.ylabel('Energy')
# plt.savefig("./CORvsENE.png")
# plt.close()
#
# plt.scatter(featuresArray[26:51, 1], featuresArray[26:51, 3], color='pink')
# plt.xlabel('Correlation')
# plt.ylabel('Homogeneity')
# plt.savefig("./CORvsHOM.png")
# plt.close()
#




# BACKUPPPPPPPPPP
# for i in range(height):
#     resultFeaturesArray = (trainFeaturesArray - testFeaturesArray[i, :])**2
#     if i < 25:
#         flag = 0
#     elif i > 25 and i < 50:
#         flag = 1
#     else:
#         flag = 2
#     for j in range(height):
#         distance = (np.sum(resultFeaturesArray[j, :3]))**(1/2)
#         auxList.append(distance)
#     distanceAsphalt = auxList[:25]
#     distanceDanger = auxList[25:50]
#     distanceGrass = auxList[50:]
#     distanceAsphalt.sort()
#     distanceDanger.sort()
#     distanceGrass.sort()
#     asphaltCounter = 0
#     dangerCounter = 0
#     grassCounter = 0
#     for counter in range(5):
#         auxList = [(distanceAsphalt[counter], 1), (distanceDanger[counter], 2), (distanceGrass[counter], 3)]
#         auxList.sort()
#         if auxList[0][1] == 1:
#             asphaltCounter += 1
#         elif auxList[0][1] == 2:
#             dangerCounter += 1
#         else:
#             grassCounter += 1
#     auxList = [(asphaltCounter, 0), (dangerCounter, 1), (grassCounter, 2)]
#     auxList.sort()
#     confusionMatrix[auxList[0][1], flag] += 1
#     auxList = []
#
# print(confusionMatrix)
#

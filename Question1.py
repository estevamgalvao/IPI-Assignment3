import cv2
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from functions.rgb_greyscale import RGB2Greyscale
from functions.featuresExtraction import *
from functions.glcm import *

#/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 3/Images/train

adress = input("Adress: ")
typeImg = input("Type of: ")
if adress == '':
    adress = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 3/Images/train"
if typeImg == '':
    adress += '/*.png'
else:
    adress += '/*.' + typeImg

# Leio as imagens da pasta e salvo em uma lista. Logo após recupero o número de imagens lidas #
imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImage = len(imageArray)

trainFeaturesArray = []
auxList = []

for k in range(numImage):
    print(k + 1)
    # print(k, end=' ')
    # print("%d" %(k+1))
    image = RGB2Greyscale(imageArray[k])
    # print(matrixGLCM)
    matrixGLCM = GLCM_Mounter(image)
    matrixGLCM /= np.sum(matrixGLCM)

    features = allFeatures(matrixGLCM)
    trainFeaturesArray.append(features)

trainFeaturesArray = np.array(trainFeaturesArray, dtype = np.float64)
print(trainFeaturesArray)
# # print(np.corrcoef(trainFeaturesArray[:, 1], trainFeaturesArray[:, 0]))
# print()
# print()
# for type in range(3):
#     if type == 1:
#         relationConCor = np.corrcoef(trainFeaturesArray[:25, 0], trainFeaturesArray[:25, 1])
#         relationConEne = np.corrcoef(trainFeaturesArray[:25, 0], trainFeaturesArray[:25, 2])
#         relationConHom = np.corrcoef(trainFeaturesArray[:25, 0], trainFeaturesArray[:25, 3])
#         relationCorEne = np.corrcoef(trainFeaturesArray[:25, 1], trainFeaturesArray[:25, 2])
#         relationCorHom = np.corrcoef(trainFeaturesArray[:25, 1], trainFeaturesArray[:25, 3])
#         relationEneHom = np.corrcoef(trainFeaturesArray[:25, 2], trainFeaturesArray[:25, 3])
#         relationList1 = [(abs(relationConCor[0, 1]), 0), (abs(relationConEne[0, 1]), 1), (abs(relationConHom[0, 1]), 2),
#                          (abs(relationCorEne[0, 1]), 3), (abs(relationCorHom[0, 1]), 4), (abs(relationEneHom[0, 1]), 5)]
#         relationList1.sort()
#     elif type == 2:
#         relationConCor = np.corrcoef(trainFeaturesArray[25:50, 0], trainFeaturesArray[25:50, 1])
#         relationConEne = np.corrcoef(trainFeaturesArray[25:50, 0], trainFeaturesArray[25:50, 2])
#         relationConHom = np.corrcoef(trainFeaturesArray[25:50, 0], trainFeaturesArray[25:50, 3])
#         relationCorEne = np.corrcoef(trainFeaturesArray[25:50, 1], trainFeaturesArray[25:50, 2])
#         relationCorHom = np.corrcoef(trainFeaturesArray[25:50, 1], trainFeaturesArray[25:50, 3])
#         relationEneHom = np.corrcoef(trainFeaturesArray[25:50, 2], trainFeaturesArray[25:50, 3])
#         relationList2 = [(abs(relationConCor[0, 1]), 0), (abs(relationConEne[0, 1]), 1), (abs(relationConHom[0, 1]), 2),
#                          (abs(relationCorEne[0, 1]), 3), (abs(relationCorHom[0, 1]), 4), (abs(relationEneHom[0, 1]), 5)]
#         relationList2.sort()
#     else:
#         relationConCor = np.corrcoef(trainFeaturesArray[50:, 0], trainFeaturesArray[50:, 1])
#         relationConEne = np.corrcoef(trainFeaturesArray[50:, 0], trainFeaturesArray[50:, 2])
#         relationConHom = np.corrcoef(trainFeaturesArray[50:, 0], trainFeaturesArray[50:, 3])
#         relationCorEne = np.corrcoef(trainFeaturesArray[50:, 1], trainFeaturesArray[50:, 2])
#         relationCorHom = np.corrcoef(trainFeaturesArray[50:, 1], trainFeaturesArray[50:, 3])
#         relationEneHom = np.corrcoef(trainFeaturesArray[50:, 2], trainFeaturesArray[50:, 3])
#         relationList3 = [(abs(relationConCor[0, 1]), 0), (abs(relationConEne[0, 1]), 1), (abs(relationConHom[0, 1]), 2),
#                          (abs(relationCorEne[0, 1]), 3), (abs(relationCorHom[0, 1]), 4), (abs(relationEneHom[0, 1]), 5)]
#         relationList3.sort()
#
#
# # print(relationList1)
# # print(relationList2)
# # print(relationList3)
#
# print()
# greatestRelation1 = relationList1[5]
# greatestRelation2 = relationList2[5]
# greatestRelation3 = relationList3[5]
#
# # print("Greatest Relation Asphalt:", greatestRelation1)
# # print("Greatest Relation Danger:", greatestRelation2)
# # print("Greatest Relation Grass:", greatestRelation3)
#
# # Contraste e Correlação #
# plt.scatter(trainFeaturesArray[:26, 0], trainFeaturesArray[:26, 1], color='blue')
# plt.scatter(trainFeaturesArray[26:51, 0], trainFeaturesArray[26:51, 1], color='red')
# plt.scatter(trainFeaturesArray[51:, 0], trainFeaturesArray[51:, 1], color='green')
# plt.xlabel('Contrast')
# plt.ylabel('Correlation')
# plt.savefig("./CONvsCOR.png")
# plt.close()
#
#
# # Contraste e Energia #
# plt.scatter(trainFeaturesArray[:26, 0], trainFeaturesArray[:26, 2], color='darkblue')
# plt.scatter(trainFeaturesArray[26:51, 0], trainFeaturesArray[26:51, 2], color='crimson')
# plt.scatter(trainFeaturesArray[51:, 0], trainFeaturesArray[51:, 2], color='darkgreen')
# plt.xlabel('Contrast')
# plt.ylabel('Energy')
# plt.savefig("./CONvsENE.png")
# plt.close()
#
#
# # Correlação e Energia #
# plt.scatter(trainFeaturesArray[:26, 1], trainFeaturesArray[:26, 2], color='lightblue')
# plt.scatter(trainFeaturesArray[26:51, 1], trainFeaturesArray[26:51, 2], color='coral')
# plt.scatter(trainFeaturesArray[51:, 1], trainFeaturesArray[51:, 2], color='lightgreen')
# plt.xlabel('Correlation')
# plt.ylabel('Energy')
# plt.savefig("./CORvsENE.png")
# plt.close()
# # plt.show()
#
# # Axes3D.plot_surface()
#

adress = input("Adress: ")
typeImg = input("Type of: ")
if adress == '':
    adress = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 3/Images/test"
if typeImg == '':
    adress += '/*.png'
else:
    adress += '/*.' + typeImg

imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImage = len(imageArray)

testFeaturesArray = []

for u in range(numImage):
    print(u + 1)
    # print("%d" %(u+1), end=' ')
    # print(u + 1)
    image = RGB2Greyscale(imageArray[u])
    # print(matrixGLCM)
    matrixGLCM = GLCM_Mounter(image)
    matrixGLCM /= np.sum(matrixGLCM)

    features = allFeatures(matrixGLCM, 3)
    testFeaturesArray.append(features)

testFeaturesArray = np.array(testFeaturesArray, dtype = np.float64)
print(testFeaturesArray)

confusionMatrix = np.array((
               [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]), dtype= np.uint8)









height, width = testFeaturesArray.shape
for i in range(height):
    resultFeaturesArray = (trainFeaturesArray - testFeaturesArray[i, :])**2
    if i < 25:
        flag = 0
    elif i > 25 and i < 50:
        flag = 1
    else:
        flag = 2
    for j in range(height):
        distance = (np.sum(resultFeaturesArray[j, :3]))**(1/2)
        auxList.append(distance)
    distanceAsphalt = auxList[:25]
    distanceDanger = auxList[25:50]
    distanceGrass = auxList[50:]
    distanceAsphalt.sort()
    distanceDanger.sort()
    distanceGrass.sort()
    asphaltCounter = 0
    dangerCounter = 0
    grassCounter = 0
    for counter in range(5):
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


# distance = np.sum()
# distanceList.append()
#
#     for a in range(25):
#
#     for d in range(25, 50):
#
#     for g in range(50, 75):
#
#


#
# resultFeaturesArray = testFeaturesArray - trainFeaturesArray
# print(resultFeaturesArray)

# print(resultFeaturesArray)






#
# testListAsphalt = []
# testListDanger = []
# testListGrass = []
# for imageTest, imageTrain in zip(testFeaturesArray, trainFeaturesArray):
#     for i in range(25):
#         distance = ((imageTest[0] - imageTrain[0]))**(1/2)
#











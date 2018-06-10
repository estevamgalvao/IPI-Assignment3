import cv2
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from functions.rgb_greyscale import RGB2Greyscale
from functions.featuresExtraction import *
from functions.glcm import *
from functions.featureSelection import featureRelation

#/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 3/Images/train

# adress = input("Train images adress: ")
# typeImg = input("Train images type: ")
adress = ''
typeImg = ''
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

for k in range(numImage):
    print(k + 1)
    image = RGB2Greyscale(imageArray[k])

    matrixGLCM = GLCM_Mounter(image)
    matrixGLCM /= np.sum(matrixGLCM)

    features = allFeatures(matrixGLCM)
    trainFeaturesArray.append(features)
trainFeaturesArray = np.array(trainFeaturesArray, dtype = np.float32)
# print(trainFeaturesArray)

featureRelation(trainFeaturesArray)

# adress = input("Test images adress: ")
# typeImg = input("Test images type: ")
adress = ''
typeImg = ''
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
    image = RGB2Greyscale(imageArray[u])

    matrixGLCM = GLCM_Mounter(image)
    matrixGLCM /= np.sum(matrixGLCM)

    features = allFeatures(matrixGLCM, 3)
    testFeaturesArray.append(features)
testFeaturesArray = np.array(testFeaturesArray, dtype = np.float32)
# print(testFeaturesArray)

confusionMatrix = np.array((
               [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]), dtype= np.uint8)
height, width = testFeaturesArray.shape

distanceList = []
auxList = []

for i in range(height):
    resultFeaturesArray = (trainFeaturesArray - testFeaturesArray[i, :]) ** 2
    if i < 25:
        flagTrue = 0
    elif i > 25 and i < 51:
        flagTrue = 1
    else:
        flagTrue = 2

    for j in range(height):
        if j < 25:
            flag = 0
        elif j > 25 and j < 51:
            flag = 1
        else:
            flag = 2
        distance = (np.sum(resultFeaturesArray[j, :3])) ** (1 / 2)
        distanceList.append((distance, flag))
    distanceAsphalt = distanceList[:25]
    distanceDanger = distanceList[25:50]
    distanceGrass = distanceList[50:]

    distanceAsphalt.sort()
    distanceDanger.sort()
    distanceGrass.sort()
    distanceList.sort()

    asphaltCounter = 0
    dangerCounter = 0
    grassCounter = 0
    for counter in range(1):
        if distanceList[counter][1] == 0:
            asphaltCounter += 1
        elif distanceList[counter][1] == 1:
            dangerCounter += 1
        elif distanceList[counter][1] == 2:
            grassCounter += 1
    auxList = [(asphaltCounter, 0), (dangerCounter, 1), (grassCounter, 2)]
    auxList.sort()
    confusionMatrix[auxList[2][1], flagTrue] += 1
    distanceList = []

print(confusionMatrix)

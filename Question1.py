import cv2
import glob
import datetime

from functions.rgb_greyscale import RGB2Greyscale
from functions.featureSelection import featureRelation
from functions.featuresExtraction import *
from functions.glcm import *
from functions.miscellaneous import *

#/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 3/Images/train
a = datetime.datetime.now()

adress = input("Train images adress: ")
typeImg = input("Train images type: ")
adress = confirmAdress(adress, typeImg)

# Leio as imagens da pasta e salvo em uma lista. Logo após recupero o número de imagens lidas #
imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImage = len(imageArray)

#########################################################
# PROCESSAMENTO DAS GLCMS E SELEÇÃO DAS CARACTERÍSTICAS #
#########################################################

trainFeaturesArray = []
print("\nProcessing...\n")
# Para cada imagem eu a transformo em cinza, adquiro sua matriz GLCM e suas respectivas features, então as guardo em um Array #
for k in range(numImage):
    # print(k + 1)
    image = RGB2Greyscale(imageArray[k])

    matrixGLCM = GLCM_Mounter(image)
    matrixGLCM /= np.sum(matrixGLCM)

    features = allFeatures(matrixGLCM)
    trainFeaturesArray.append(features)
# Converto esse Array para um np.array afim de facilitar operações e vizualização #
trainFeaturesArray = np.array(trainFeaturesArray, dtype = np.float32)
# print(trainFeaturesArray)

# Descubro qual feature devo ignorar #

featureRelation(trainFeaturesArray)

adress = input("Test images adress: ")
typeImg = input("Test images type: ")
adress = confirmAdress(adress, typeImg)
print(adress)

imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImage = len(imageArray)

testFeaturesArray = []

print("\nProcessing...\n")
for u in range(numImage):
    image = RGB2Greyscale(imageArray[u])

    matrixGLCM = GLCM_Mounter(image)
    matrixGLCM /= np.sum(matrixGLCM)

    features = allFeatures(matrixGLCM, 3) # Não calculo a feature eliminada #
    testFeaturesArray.append(features)

testFeaturesArray = np.array(testFeaturesArray, dtype = np.float32)

######################################################
# CÁLCULO DAS DISTÂNCIAS E CLASSIFICAÇÃO DAS IMAGENS #
######################################################

confusionMatrix = np.array((
               [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]), dtype= np.uint8)
height, width = testFeaturesArray.shape

distanceList = []
auxList = []

for i in range(height):
    # Supondo que distancia = (Δx² + Δy² + Δz²)^(1/2)
    # Crio um array do tipo [Δx1²   Δy1²   Δz1² ]
    #                               :
    #                               :
    #                       [Δx75²  Δy75²  Δz75²]
    resultFeaturesArray = (trainFeaturesArray - testFeaturesArray[i, :]) ** 2
    # Crio uma flag pra saber o tipo real da imagem
    if i < 25:
        flagTrue = 0
    elif i > 25 and i < 51:
        flagTrue = 1
    else:
        flagTrue = 2

    for j in range(height):
    # Crio outra flag pra saber o tipo que a imagem foi classificada
        if j < 25:
            flag = 0
        elif j > 25 and j < 51:
            flag = 1
        else:
            flag = 2
        distance = (np.sum(resultFeaturesArray[j, :3])) ** (1 / 2) # Calculo a raiz quadrada da soma dos meus Δ
        distanceList.append((distance, flag)) # Marco com uma flag pra saber de qual conjunto é essa distância #
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
    for counter in range(8): # Vou contando o número de vizinhos perto do ponto que está sendo classificado #
        if distanceList[counter][1] == 0:
            asphaltCounter += 1
        elif distanceList[counter][1] == 1:
            dangerCounter += 1
        elif distanceList[counter][1] == 2:
            grassCounter += 1
    auxList = [(asphaltCounter, 0), (dangerCounter, 1), (grassCounter, 2)]
    auxList.sort()
    confusionMatrix[auxList[2][1], flagTrue] += 1 # Marco isso na matriz com a flag que eu classifiquei e a flag de verdade #
    distanceList = []

b = datetime.datetime.now()

printConfusionMatrix(confusionMatrix)
print("The program took %d hours, %d minutes and %d seconds to finish the classification"%(abs(b.hour-a.hour), abs(b.minute-a.minute), abs(b.second-a.second)))
import cv2
import glob
from functions.rgb_greyscale import RGB2Greyscale
from functions.featuresExtraction import *
from functions.glcm import *

#/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 3/Images/train

adress = input("Adress: ")
typeImg = input("Type of: ")
if adress == '':
    adress = "/home/estevamgalvao/Documentos/PycharmProjects/IPI-Assignment3/images"
if typeImg == '':
    adress += '/*.tif'
else:
    adress += '/*.' + typeImg

# Leio as imagens da pasta e salvo em uma lista. Logo após recupero o número de imagens lidas #
imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImage = len(imageArray)

featuresArray = []
auxList = []

for k in range(numImage):
    print(k+1)
    image = RGB2Greyscale(imageArray[k])
    # print(matrixGLCM)
    matrixGLCM = GLCM_Mounter(image)
    matrixGLCM /= np.sum(matrixGLCM)

    features = allFeatures(matrixGLCM)
    # print(features)
    featuresArray.append(features)
# featuresArray.append([1, 1.1, 1.2, 1.3])

print()
print()
# print(featuresArray)
featuresArray = np.array(featuresArray, dtype = np.float64)

# aC = np.corrcoef(featuresArray[:26, 0], featuresArray[:26, 1])
# auxList.append(aC[0, 1])

print(np.corrcoef(featuresArray[:, 1], featuresArray[:, 0]))

for type in range(3):
    if type == 1:
        relationConCor = np.corrcoef(featuresArray[:26, 0], featuresArray[:26, 1])
        relationConEne = np.corrcoef(featuresArray[:26, 0], featuresArray[:26, 2])
        relationConHom = np.corrcoef(featuresArray[:26, 0], featuresArray[:26, 3])
        relationCorEne = np.corrcoef(featuresArray[:26, 1], featuresArray[:26, 2])
        relationCorHom = np.corrcoef(featuresArray[:26, 1], featuresArray[:26, 3])
        relationEneHom = np.corrcoef(featuresArray[:26, 2], featuresArray[:26, 3])
    elif type == 2:
        relationConCor = np.corrcoef(featuresArray[26:51, 0], featuresArray[26:51, 1])
        relationConEne = np.corrcoef(featuresArray[26:51, 0], featuresArray[26:51, 2])
        relationConHom = np.corrcoef(featuresArray[26:51, 0], featuresArray[26:51, 3])
        relationCorEne = np.corrcoef(featuresArray[26:51, 1], featuresArray[26:51, 2])
        relationCorHom = np.corrcoef(featuresArray[26:51, 1], featuresArray[26:51, 3])
        relationEneHom = np.corrcoef(featuresArray[26:51, 2], featuresArray[26:51, 3])
    else:
        relationConCor = np.corrcoef(featuresArray[51:, 0], featuresArray[51:, 1])
        relationConEne = np.corrcoef(featuresArray[51:, 0], featuresArray[51:, 2])
        relationConHom = np.corrcoef(featuresArray[51:, 0], featuresArray[51:, 3])
        relationCorEne = np.corrcoef(featuresArray[51:, 1], featuresArray[51:, 2])
        relationCorHom = np.corrcoef(featuresArray[51:, 1], featuresArray[51:, 3])
        relationEneHom = np.corrcoef(featuresArray[51:, 2], featuresArray[51:, 3])
    auxList = [abs(relationConCor[0, 1]), abs(relationConEne[0, 1]), abs(relationConHom[0, 1]), abs(relationCorEne[0, 1]), abs(relationCorHom[0, 1]), abs(relationEneHom[0, 1])]
    print(auxList)
    print()
greatestRelation = (auxList[0], 0)
for r in range(1, len(auxList)):
    if auxList[r] > greatestRelation[0]:
        greatestRelation = (auxList[r], r)
print(greatestRelation)

# Característica a ser excluída = auxList[greatesRelation(1)]
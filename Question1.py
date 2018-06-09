import cv2
import glob
import matplotlib.pyplot as plt
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
    featuresArray.append(features)

print()
print()

featuresArray = np.array(featuresArray, dtype = np.float64)
print(featuresArray)
# print(np.corrcoef(featuresArray[:, 1], featuresArray[:, 0]))
print()
print()
for type in range(3):
    if type == 1:
        relationConCor = np.corrcoef(featuresArray[:26, 0], featuresArray[:26, 1])
        relationConEne = np.corrcoef(featuresArray[:26, 0], featuresArray[:26, 2])
        relationConHom = np.corrcoef(featuresArray[:26, 0], featuresArray[:26, 3])
        relationCorEne = np.corrcoef(featuresArray[:26, 1], featuresArray[:26, 2])
        relationCorHom = np.corrcoef(featuresArray[:26, 1], featuresArray[:26, 3])
        relationEneHom = np.corrcoef(featuresArray[:26, 2], featuresArray[:26, 3])
        relationList1 = [(abs(relationConCor[0, 1]), 0), (abs(relationConEne[0, 1]), 1), (abs(relationConHom[0, 1]), 2),
                         (abs(relationCorEne[0, 1]), 3), (abs(relationCorHom[0, 1]), 4), (abs(relationEneHom[0, 1]), 5)]
        relationList1.sort()
    elif type == 2:
        relationConCor = np.corrcoef(featuresArray[26:51, 0], featuresArray[26:51, 1])
        relationConEne = np.corrcoef(featuresArray[26:51, 0], featuresArray[26:51, 2])
        relationConHom = np.corrcoef(featuresArray[26:51, 0], featuresArray[26:51, 3])
        relationCorEne = np.corrcoef(featuresArray[26:51, 1], featuresArray[26:51, 2])
        relationCorHom = np.corrcoef(featuresArray[26:51, 1], featuresArray[26:51, 3])
        relationEneHom = np.corrcoef(featuresArray[26:51, 2], featuresArray[26:51, 3])
        relationList2 = [(abs(relationConCor[0, 1]), 0), (abs(relationConEne[0, 1]), 1), (abs(relationConHom[0, 1]), 2),
                         (abs(relationCorEne[0, 1]), 3), (abs(relationCorHom[0, 1]), 4), (abs(relationEneHom[0, 1]), 5)]
        relationList2.sort()
    else:
        relationConCor = np.corrcoef(featuresArray[51:, 0], featuresArray[51:, 1])
        relationConEne = np.corrcoef(featuresArray[51:, 0], featuresArray[51:, 2])
        relationConHom = np.corrcoef(featuresArray[51:, 0], featuresArray[51:, 3])
        relationCorEne = np.corrcoef(featuresArray[51:, 1], featuresArray[51:, 2])
        relationCorHom = np.corrcoef(featuresArray[51:, 1], featuresArray[51:, 3])
        relationEneHom = np.corrcoef(featuresArray[51:, 2], featuresArray[51:, 3])
        relationList3 = [(abs(relationConCor[0, 1]), 0), (abs(relationConEne[0, 1]), 1), (abs(relationConHom[0, 1]), 2),
                         (abs(relationCorEne[0, 1]), 3), (abs(relationCorHom[0, 1]), 4), (abs(relationEneHom[0, 1]), 5)]
        relationList3.sort()

greatestRelation1 = relationList1[5]
greatestRelation2 = relationList2[5]
greatestRelation3 = relationList3[5]

print("Greatest Relation Asphalt:", greatestRelation1)
print("Greatest Relation Danger:", greatestRelation2)
print("Greatest Relation Grass:", greatestRelation3)

# ASFALTO E GRAMA #
plt.scatter(featuresArray[:26, 0], featuresArray[:26, 2], color='blue')
plt.scatter(featuresArray[51:, 0], featuresArray[51:, 2], color='red')
plt.xlabel('Contrast')
plt.ylabel('Energy')
plt.savefig("./CONvsENE.png")
plt.close()

plt.scatter(featuresArray[:26, 0], featuresArray[:26, 3], color='yellow')
plt.scatter(featuresArray[51:, 0], featuresArray[51:, 3], color='purple')
plt.xlabel('Contrast')
plt.ylabel('Homogeneity')
plt.savefig("./CONvsHOM.png")
plt.close()

# TODOS #
plt.scatter(featuresArray[:26, 2], featuresArray[:26, 3], color='orange')
plt.scatter(featuresArray[51:, 2], featuresArray[51:, 3], color='green')
plt.scatter(featuresArray[26:51, 2], featuresArray[26:51, 3], color='brown')
plt.xlabel('Energy')
plt.ylabel('Homogeneity')
plt.savefig("./ENEvsHOM.png")
plt.close()


# PERIGO #
plt.scatter(featuresArray[26:51, 1], featuresArray[26:51, 2], color='black')
plt.xlabel('Correlation')
plt.ylabel('Energy')
plt.savefig("./CORvsENE.png")
plt.close()

plt.scatter(featuresArray[26:51, 1], featuresArray[26:51, 3], color='pink')
plt.xlabel('Correlation')
plt.ylabel('Homogeneity')
plt.savefig("./CORvsHOM.png")
plt.close()


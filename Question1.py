import cv2
import numpy as np
import glob
from functions.rgb_greyscale import RGB2Greyscale
from functions.featuresExtraction import *

adress = input("Adress: ")
typeImg = input("Type of: ")

if adress == '':
    adress = "/home/estevamgalvao/Documentos/PycharmProjects/IPI-Assignment3/images"

if typeImg == '':
    adress += '/*.tif'
else:
    adress += '/*' + typeImg

# Leio as imagens da pasta e salvo em uma lista. Logo após recupero o número de imagens lidas #
imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImage = len(imageArray)

height, width, channels = imageArray[0].shape

arrayGLCM_Dictionary = []
arrayGLCM_Matrix = []
arrayImage_Histogram = []

listHistogram = []
for image in imageArray:
    image = RGB2Greyscale(image)
    glcmDictionary = {}
    imageHistogram = {}
    for i, x in zip(range(height), range(height)):
        for j, y in zip(range(width), range(width - 1)):
            pixelPair = (image[x, y], image[x, y + 1])
            if pixelPair in glcmDictionary:
                glcmDictionary[pixelPair] += 1
            else:
                glcmDictionary[pixelPair] = 1
            if image[i, j] in imageHistogram:
                imageHistogram[image[i, j]] += 1
            else:
                imageHistogram[image[i, j]] = 1
                listHistogram.insert(0, image[i, j])

    auxShape = len(listHistogram)

    matrixGLCM = np.zeros((auxShape, auxShape), dtype = np.int64)

    for n, i in zip(listHistogram,range(auxShape)):
        for m, j in zip(listHistogram, range(auxShape)):
            # print("N:", n, "i:", i, "M:", m, "j:", j)
            if (n, m) in glcmDictionary:
                # Talvez tenha que criar tuplas aqui se os índices da GLCM forem intensidades de pixels
                # matrixGLCM[i, j] = (n, m, glcmDictionary[(n, m)]) -> tipo esse -> (i, j, glcm(i, j))
                matrixGLCM[i, j] = glcmDictionary[(n, m)]

    arrayGLCM_Dictionary.append(glcmDictionary)
    arrayImage_Histogram.append(imageHistogram)
    arrayGLCM_Matrix.append(matrixGLCM)
    print(matrixGLCM)

    print("Contrast:", contrast(matrixGLCM))
    print("Correlation:", correlation(matrixGLCM))
    print("Energy:", energy(matrixGLCM))
    print("Homogeneity:", homogeneity(matrixGLCM))

#     matrixGLCM = np.array((
# [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 9, 1, 0, 0, 0, 0, 0],
#  [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
#  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0, 0, 1, 9, 1, 0],
#  [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]), dtype= np.int64)

import cv2
import numpy as np
import glob
import os
from functions.rgb_greyscale import RGB2Greyscale

adress = input("Adress: ")
if adress == 'a':
    adress = "/home/estevamgalvao/Documentos/PycharmProjects/IPI-Assignment3/images"
adress += '/*.tif'

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
    print(listHistogram)
    print(imageHistogram)

    matrixGLCM = np.zeros((auxShape, auxShape), dtype = np.uint8)

    for n, i in zip(listHistogram,range(auxShape)):
        for m, j in zip(listHistogram, range(auxShape)):
            # print("N:", n, "i:", i, "M:", m, "j:", j)
            if (n, m) in glcmDictionary:
                matrixGLCM[i, j] = glcmDictionary[(n, m)]

    arrayGLCM_Dictionary.append(glcmDictionary)
    arrayImage_Histogram.append(imageHistogram)
    arrayGLCM_Matrix.append(matrixGLCM)
    print(matrixGLCM)
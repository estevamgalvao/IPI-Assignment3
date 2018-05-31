def contraste(matriz, shape):
    cont = 0
    for i in range(shape):
        for j in range(shape):
            cont += (abs(i - j) ** 2) * matriz[i, j]
            if matriz[i, j] != 0:
                print(i, j, matriz[i, j])
    return cont


def energia(matriz, shape):
    energ = 0
    for i in range(shape):
        for j in range(shape):
            energ += matriz[i, j] ** 2
    return energ


def homogenidade(matriz, shape):
    homo = 0
    for i in range(shape):
        for j in range(shape):
            homo += matriz[i, j] / (1 + abs(i - j))
    return homo


def correlacao(matriz, shape, dic):
    def valorLinha(linha, matriz):
        valor = 0
        for j in range(shape):
            valor += matriz[linha, j]
        return valor

    def valorColuna(coluna, matriz):
        valor = 0
        for i in range(shape):
            valor += matriz[i, coluna]
        return valor

    def pesosLinha(matriz):
        valor = 0
        for i in range(1, shape):
            valor += i * valorLinha(i - 1, matriz)
        return valor

    def pesosColuna(matriz):
        valor = 0
        for j in range(1, shape):
            valor += j * valorLinha(j - 1, matriz)
        return valor

    correla = 0
    for i in range(shape):
        for j in range(shape):
            a = pesosLinha(dic)
            b = pesosColuna(dic)
            correla += (((i - a) * (j - b)) * matriz[i, j]) / (a * b)
    return correla


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

image = imageArray[0]
height, width, channels = image.shape
glcmArray = []

for image in imageArray:
    image = RGB2Greyscale(image)
    dicGLCM = {}
    # print(image)
    # Faço for height e depois for width pois quero que o bloco 2x1 ande da esquerda para direta
    # e não de cima pra baixo
    for i in range(height):
        for j in range(width - 1):
            # print(image[0, 0])
            auxTuple = (image[i, j], image[i, j + 1])
            if auxTuple in dicGLCM:
                dicGLCM[auxTuple] += 1
            else:
                dicGLCM[auxTuple] = 1
    glcmArray.append(dicGLCM)

histogram = {}
listHistogram = []
for i in range(height):
    for j in range(width):
        if image[i, j] in histogram:
            histogram[image[i, j]] += 1
        else:
            histogram[image[i, j]] = 1
            listHistogram.insert(0, image[i, j])

auxShape = len(listHistogram)
print(listHistogram)

matrixGLCM = np.zeros((auxShape, auxShape), dtype = np.uint8)

for n, i in zip(listHistogram,range(auxShape)):
    for m, j in zip(listHistogram, range(auxShape)):
        # print("N:", n, "i:", i, "M:", m, "j:", j)
        if (n, m) in dicGLCM:
            matrixGLCM[i, j] = dicGLCM[(n, m)]

print(matrixGLCM)
# print(matrixGLCM[:, :])
print(contraste(matrixGLCM, auxShape))
print(energia(matrixGLCM, auxShape))
print(homogenidade(matrixGLCM, auxShape))
# print(correlacao(matrixGLCM, auxShape, dicGLCM))
import cv2
import numpy as np
import glob
import os

adress = input()
adress += '*.bmp'
# Leio as imagens da pasta e salvo em uma lista. Logo após recupero o número de imagens lidas #
imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImage = len(imageArray)

image = imageArray[0]
height, width, channels = imageArray[0].shape

glcmArray = []
for image in imageArray:
    dicGLCM = {}
    # Faço for height e depois for width pois quero que o bloco 2x1 ande da esquerda para direta
    # e não de cima pra baixo
    for i in range(height):
        for j in range(width - 1):
            auxTuple = (image[i, j], image[i, j + 1])
            if auxTuple in dicGLCM:
                dicGLCM[auxTuple] += 1
            else:
                dicGLCM[auxTuple] = 1
    glcmArray.append(dicGLCM)

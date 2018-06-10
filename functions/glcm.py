import numpy as np

def GLCM_HistDictionary(image):
    height, width = image.shape
    listHistogram = []
    imageHistogram = {}
    glcmDictionary = {}
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
    listHistogram.sort()
    return [listHistogram, imageHistogram, glcmDictionary]

def GLCM_Mounter(image):
    listHistogram, imageHistogram, glcmDictionary = GLCM_HistDictionary(image)
    auxShape = len(listHistogram)

    matrixGLCM = np.zeros((auxShape, auxShape), dtype=np.float32)

    for n, i in zip(listHistogram, range(auxShape)):
        for m, j in zip(listHistogram, range(auxShape)):
            if (n, m) in glcmDictionary:
                # Talvez tenha que criar tuplas aqui se os índices da GLCM forem intensidades de pixels
                # matrixGLCM[i, j] = (n, m, glcmDictionary[(n, m)]) -> tipo esse -> (i, j, glcm(i, j))
                matrixGLCM[i, j] = glcmDictionary[(n, m)]

    return matrixGLCM


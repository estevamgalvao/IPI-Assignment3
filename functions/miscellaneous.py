import numpy as np

def confirmAdress(adress = '', typeImg = ''):
    if adress == '':
        adress = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 3/Images/train"
    elif adress == 'a':
        adress = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 3/Images/test"
    if typeImg == '':
        adress += '/*.png'
    else:
        adress += '/*.' + typeImg
    return adress

def printConfusionMatrix(confusionMatrix):
    precision = float((confusionMatrix[0, 0] + confusionMatrix[1, 1] + confusionMatrix[2, 2]) / np.sum(confusionMatrix))
    print("\nReal           \tAsphalt\tDanger\tGrass")
    print("Classified")
    print("Asphalt\t        %d\t    %d\t    %d" % (confusionMatrix[0, 0], confusionMatrix[0, 1], confusionMatrix[0, 2]))
    print("Danger\t        %d\t    %d\t    %d" % (confusionMatrix[1, 0], confusionMatrix[1, 1], confusionMatrix[1, 2]))
    print("Grass\t        %d\t    %d\t    %d" % (confusionMatrix[2, 0], confusionMatrix[2, 1], confusionMatrix[2, 2]))
    print("\nPrecision: %.2f%%" % (precision))
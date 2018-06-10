import numpy as np
import matplotlib.pyplot as plt

# Faço a relação de todas as features entre os três tipos de terreno #
# 1 = Asfalto, primeiras 25 imagens #
# 2 = Perigo, próximas 25 imagens #
# 3 = Grama, próximas 25 imagens #
# Com esses valores, seleciono o maior valor de cada terreno e identifico a característica em comum nas 3 relações, então a elimino #

def featureRelation(featuresArray):
    for type in range(3):
        if type == 1:
            relationConCor = np.corrcoef(featuresArray[:25, 0], featuresArray[:25, 1])
            relationConEne = np.corrcoef(featuresArray[:25, 0], featuresArray[:25, 2])
            relationConHom = np.corrcoef(featuresArray[:25, 0], featuresArray[:25, 3])
            relationCorEne = np.corrcoef(featuresArray[:25, 1], featuresArray[:25, 2])
            relationCorHom = np.corrcoef(featuresArray[:25, 1], featuresArray[:25, 3])
            relationEneHom = np.corrcoef(featuresArray[:25, 2], featuresArray[:25, 3])
            relationList1 = [(abs(relationConCor[0, 1]), 'Contrast&Correlation'), (abs(relationConEne[0, 1]), 'Contrast&Energy'), (abs(relationConHom[0, 1]), 'Contrast&Homogeneity'),
                             (abs(relationCorEne[0, 1]), 'Correlation&Energy'), (abs(relationCorHom[0, 1]), 'Correlation&Homogeneity'), (abs(relationEneHom[0, 1]), 'Energy&Homogeneity')]
            relationList1.sort()
        elif type == 2:
            relationConCor = np.corrcoef(featuresArray[25:50, 0], featuresArray[25:50, 1])
            relationConEne = np.corrcoef(featuresArray[25:50, 0], featuresArray[25:50, 2])
            relationConHom = np.corrcoef(featuresArray[25:50, 0], featuresArray[25:50, 3])
            relationCorEne = np.corrcoef(featuresArray[25:50, 1], featuresArray[25:50, 2])
            relationCorHom = np.corrcoef(featuresArray[25:50, 1], featuresArray[25:50, 3])
            relationEneHom = np.corrcoef(featuresArray[25:50, 2], featuresArray[25:50, 3])
            relationList2 = [(abs(relationConCor[0, 1]), 'Contrast&Correlation'), (abs(relationConEne[0, 1]), 'Contrast&Energy'), (abs(relationConHom[0, 1]), 'Contrast&Homogeneity'),
                             (abs(relationCorEne[0, 1]), 'Correlation&Energy'), (abs(relationCorHom[0, 1]), 'Correlation&Homogeneity'), (abs(relationEneHom[0, 1]), 'Energy&Homogeneity')]
            relationList2.sort()
        else:
            relationConCor = np.corrcoef(featuresArray[50:, 0], featuresArray[50:, 1])
            relationConEne = np.corrcoef(featuresArray[50:, 0], featuresArray[50:, 2])
            relationConHom = np.corrcoef(featuresArray[50:, 0], featuresArray[50:, 3])
            relationCorEne = np.corrcoef(featuresArray[50:, 1], featuresArray[50:, 2])
            relationCorHom = np.corrcoef(featuresArray[50:, 1], featuresArray[50:, 3])
            relationEneHom = np.corrcoef(featuresArray[50:, 2], featuresArray[50:, 3])
            relationList3 = [(abs(relationConCor[0, 1]), 'Contrast&Correlation'), (abs(relationConEne[0, 1]), 'Contrast&Energy'), (abs(relationConHom[0, 1]), 'Contrast&Homogeneity'),
                             (abs(relationCorEne[0, 1]), 'Correlation&Energy'), (abs(relationCorHom[0, 1]), 'Correlation&Homogeneity'), (abs(relationEneHom[0, 1]), 'Energy&Homogeneity')]
            relationList3.sort()

    greatestRelation1 = relationList1[5]
    greatestRelation2 = relationList2[5]
    greatestRelation3 = relationList3[5]

    print("Greatest Relation Asphalt: \nValue:[",greatestRelation1[0],"]  Relation[",greatestRelation1[1],"]")
    print("Greatest Relation Danger: \nValue:[",greatestRelation2[0],"]  Relation[",greatestRelation2[1],"]")
    print("Greatest Relation Grass: \nValue:[",greatestRelation3[0],"]  Relation[",greatestRelation3[1],"]")
    print()

    # Contraste e Correlação #
    plt.scatter(featuresArray[:26, 0], featuresArray[:26, 1], color='blue')
    plt.scatter(featuresArray[26:51, 0], featuresArray[26:51, 1], color='red')
    plt.scatter(featuresArray[51:, 0], featuresArray[51:, 1], color='green')
    plt.xlabel('Contrast')
    plt.ylabel('Correlation')
    plt.savefig("./CONvsCOR.png")
    plt.close()

    # Contraste e Energia #
    plt.scatter(featuresArray[:26, 0], featuresArray[:26, 2], color='darkblue')
    plt.scatter(featuresArray[26:51, 0], featuresArray[26:51, 2], color='crimson')
    plt.scatter(featuresArray[51:, 0], featuresArray[51:, 2], color='darkgreen')
    plt.xlabel('Contrast')
    plt.ylabel('Energy')
    plt.savefig("./CONvsENE.png")
    plt.close()

    # Correlação e Energia #
    plt.scatter(featuresArray[:26, 1], featuresArray[:26, 2], color='lightblue')
    plt.scatter(featuresArray[26:51, 1], featuresArray[26:51, 2], color='coral')
    plt.scatter(featuresArray[51:, 1], featuresArray[51:, 2], color='lightgreen')
    plt.xlabel('Correlation')
    plt.ylabel('Energy')
    plt.savefig("./CORvsENE.png")
    plt.close()
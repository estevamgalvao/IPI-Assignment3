import numpy as np

def F_measure(confusionMatrix):
    safetyMatrix = np.zeros((2, 2), dtype=np.uint8)

    safetyMatrix[0, 0] = confusionMatrix[0, 0]
    safetyMatrix[0, 1] = confusionMatrix[0, 1] + confusionMatrix[0, 2]
    safetyMatrix[1, 0] = confusionMatrix[1, 0] + confusionMatrix[2, 0]
    safetyMatrix[1, 1] = confusionMatrix[1, 1] + confusionMatrix[1, 2] + confusionMatrix[2, 1] + confusionMatrix[2, 2]

    precisionSafe = safetyMatrix[0, 0]
    precisionSafe /= float(np.sum(safetyMatrix[0]))

    recallSafe = safetyMatrix[0, 0]
    recallSafe /= float(np.sum(safetyMatrix[:, 0]))

    precisionUnsafe = safetyMatrix[1, 1]
    precisionUnsafe /= float(np.sum(safetyMatrix[1]))

    recallUnsafe = safetyMatrix[1, 1]
    recallUnsafe /= float(np.sum(safetyMatrix[:, 1]))

    F_measureSafe = 2 * (precisionSafe * recallSafe) / (precisionSafe + recallSafe)
    F_measureUnsafe = 2 * (precisionUnsafe * recallUnsafe) / (precisionUnsafe + recallUnsafe)

    return [safetyMatrix,F_measureSafe, F_measureUnsafe]

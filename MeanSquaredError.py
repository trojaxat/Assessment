import numpy as np


def calculate(actualData, predictedData):
    actualData, predictedData = np.array(actualData), np.array(predictedData)
    return np.square(np.subtract(actualData, predictedData)).mean()

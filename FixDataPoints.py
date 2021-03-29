def changeValueA(actualDataFrame, changeValue):
    predictedData = actualDataFrame.copy()
    predictedData["y"] = [item*changeValue for item in actualDataFrame["x"]]
    return predictedData


def changeValueB(actualDataFrame, changeValue):
    predictedData = actualDataFrame.copy()
    predictedData["y"] = [item+changeValue for item in actualDataFrame["x"]]
    return predictedData

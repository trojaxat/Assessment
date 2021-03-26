def changeValueA(actualDataFrame, changeValue):
    predictedData = actualDataFrame
    predictedData["y"] = [item*changeValue for item in actualDataFrame["x"]]
    return predictedData


def changeValueB(actualDataFrame, changeValue):
    predictedData = actualDataFrame
    predictedData["y"] = [item+changeValue for item in actualDataFrame["x"]]
    return predictedData

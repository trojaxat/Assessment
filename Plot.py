import pandas as pd


def getDataFrame(filename):
    return pd.read_csv(filename)


def getPlot(dataFrame, kind):
    return dataFrame.plot(kind=kind, x='x', y='y')


def constLine(x, c):
    y = x + c
    return y

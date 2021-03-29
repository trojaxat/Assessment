import MeanSquaredError
import FixDataPoints
import math


def refine(actualDataFrame, value, iterations, increment, equationPart):
    currentMeanSquareErrorValue = float("inf")
    i = 0
    while i < iterations:
        i += 1
        value = value - increment

        # re-calculate y data using the modified value
        if equationPart == "a":
            predictedData = FixDataPoints.changeValueA(actualDataFrame, value)
        elif equationPart == "b":
            predictedData = FixDataPoints.changeValueB(actualDataFrame, value)

        # update mse value
        mse = MeanSquaredError.calculate(actualDataFrame, predictedData)

        if mse < currentMeanSquareErrorValue:
            currentMeanSquareErrorValue = mse
            returnValue = value

    return {"value": '{0:.2g}'.format(returnValue), "mse": currentMeanSquareErrorValue}

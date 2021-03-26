import MeanSquaredError
import FixDataPoints


def refine(actualDataFrame, value, iterations, increment, equationPart):
    currentMeanSquareErrorValue = float("inf")
    i = 0
    while i < iterations:
        i += 1
        value = value - increment

        # re-calculate y data using the modified value
        if equationPart == "a":
            data = FixDataPoints.changeValueA(actualDataFrame, value)
        elif equationPart == "b":
            print("We are changing b")
            data = FixDataPoints.changeValueB(actualDataFrame, value)

        # update mse value
        mse = MeanSquaredError.calculate(actualDataFrame, data)
        print('mse: ', actualDataFrame)
        print('mse: ', data)
        if mse < currentMeanSquareErrorValue:
            currentMeanSquareErrorValue = mse

    return {"value": value, "mse": currentMeanSquareErrorValue}

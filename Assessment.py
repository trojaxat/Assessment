import numpy as np
import matplotlib.pyplot as plt
import Plot
import MeanSquaredError
import RefineValue
import FixDataPoints

issues to fix - fix mse value in loop and fix
# Task 1 - Read the x/y data points
actualDataFrame = Plot.getDataFrame("datapoints.csv")

# Task 2 - Create a scatterplot
plot = Plot.getPlot(actualDataFrame, "scatter")

# Task 3 - Set the slope a to 10 and the intercept b to 0. Calculate y for every value of x
predictedData = FixDataPoints.changeValueA(actualDataFrame, 10)
plt.plot(predictedData["x"], predictedData["y"], c='m')


# Task 4 - Calculate the Mean Squared Error (MSE)
MeanSquaredError.calculate(actualDataFrame, predictedData)

# Task 5 - Find a value for a that gives the lowest possible MSE
refinedMSE = RefineValue.refine(actualDataFrame, 10, 100, 0.1, "a")
print("Final a: " + str(refinedMSE["value"]) +
      "and mse: " + str(refinedMSE["mse"]))

# Task 6 - modify b
refinedMSE = RefineValue.refine(actualDataFrame, 10, 100, 0.1, "b")
print("Final b: " + str(refinedMSE["value"]) +
      "and mse: " + str(refinedMSE["mse"]))

# Task 7 - How could the algorithm be improved?
improvementIdea1 = "A and B can impact one another, it would be better to try for each 0.1 increment of a, all the increment options of b etc etc"
improvementIdea2 = "Once a range of A and B has been found, we could refine it further, the increment could be tested at 0.001 for a more precise result"
improvementIdea3 = "MSE seems to be uncommonly used, rather RMSE, it could be looked into if this would be more accurate for our dataset"

plt.show()

"""
Below is an example on how to use the object mlp_model along with it's
functionalities. Can remove quotes to test.
"""
from forecasting import MlpModel

print("\n")
# Represents time series data in form of list
time_series = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Represents the number of data points
# desired in a sample when splitting data.
# See split_data comment for further details.
# Going to ask Flores what this should be for
# differing TS data.
steps = 3
# Creates the mlp_model and assigns it to example
example = MlpModel(time_series, steps)
# Printing the output of what split_data() did to original data
for i in range(len(example.X)):
    print(example.X[i], example.y[i])

# Fitting data (must do this before forecasting)
# parameters will always be example.X and example.y
example.mlp.fit(example.X, example.y)

input = [20, 30, 40]

print("\n")

# Prints forecast for an inputted sequence
print("Forecast for",
      input, ":", example.forecast(input))

print("\n")


"""
Below is an example on how to use the object mlp_model along with it's
functionalities. Can remove quotes to test.
"""
from forecasting import MlpModel
import pandas as pd


def read_file(csv_fname: str):
    """ Reads a CSV file and converts it to a time series."""

    # reads the csv file
    # head = 0 to specify header information at row 0
    # index_col = 0 to show that first column contains index info
    # squeeze=True because we only have one data column and want a time series
    # this converts ts to a time series
    ts = pd.read_csv(csv_fname, header=0, squeeze=True)

    return ts


def ts_to_list(ts):
    """ Converts time series object to a list for visualization. 
        Returns list. """

    ts_as_list = ts.values.tolist()

    return ts_as_list


print("\n")
# Represents time series data in form of list
# time_series = [10, 20, 30, 40, 50, 60, 70, 80, 90]
time_series = ts_to_list(
    read_file("./time_series_data/3_passengers_train.csv"))

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
# example.mlp.fit(example.X, example.y)
example.fitt()

input = [100, 200, 300]

print("\n")

# Prints forecast for an inputted sequence
print("Forecast for",
      input, ":", example.forecast(input))

print("\n")

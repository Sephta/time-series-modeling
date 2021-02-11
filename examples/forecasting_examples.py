
"""
Below is an example on how to use the object mlp_model along with it's
functionalities. Can remove quotes to test.
"""
from forecasting import MlpModel
import pandas as pd
from sklearn.preprocessing import StandardScaler


def standardize(ts):
    """
    Produces a time series whose mean is 0 and variance is 1.
    """
    # Scales values
    print(ts)
    values = ts.values
    values = values.reshape((len(values), 1))
    scaler = StandardScaler()
    scaler = scaler.fit(values)

    # Converts scaled values from an array to a list
    normalized = scaler.transform(values)
    print(normalized)
    normalized_list = normalized.tolist()
    print(normalized_list)

    # Converts list to a time series
    df = pd.Series(normalized_list)
    print("TS:\n", df)
    return df


print("\n")
# Represents time series data in form of list
# time_series = [10, 20, 30, 40, 50, 60, 70, 80, 90]
time_series = pd.read_csv(
    './time_series_data/3_passengers_test.csv', header=None, squeeze=True)
time_series = standardize(time_series).values.tolist()
# print("Time series standardized:", time_series)

# Represents the number of data points
# desired in a sample when splitting data.
# See split_data comment for further details.
# Going to ask Flores what this should be for
# differing TS data.
steps = 2
# Creates the mlp_model and assigns it to example
example = MlpModel(time_series, steps)
# Printing the output of what split_data() did to original data
for i in range(len(example.X)):
    print(example.X[i], example.y[i])

# Fitting data (must do this before forecasting)
# parameters will always be example.X and example.y
example.mlp.fit(example.X, example.y)

print("\n")

# Prints forecast for an inputted sequence
print("Forecast for",
      example.X, ":", example.forecast(example.X))

print("\n")

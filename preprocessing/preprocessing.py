#!/usr/bin/env/python

""" 
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis

Utility: preprocessing functions for reading data files
and preparing them for visualization.

Note: pandas and sklearn must be downloaded in order to use this 
software. 
"""

# import statements below
import sys
import pandas as pd
from sklearn.preprocessing import *
import matplotlib.pyplot as plt

__authors__ = "Stephanie Schofield"
__version__ = "1.0.0"
__emails__ = "sschofie@cs.uoregon.edu"
__credits__ = "Ronny Fuentes, Kyra Novitzky, Alec Springel, Seth Tal"
__date__ = "01/22/2021"


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


def denoise(ts):
    """ Removes noise from times series. Takes in
    time series list, processes using modules and 
    moving median from Pandas library. """

    # converts series data points into the median of the window
    # with the max window being the length of the data
    # min_periods = 1 for the minimum amount of data required
    # at a given series position
    denoised = ts.rolling(len(ts), min_periods=1).median()

    # cannot have denoised as a list because all other preprocessing
    # functions take a time series, so kyra/ronny can use the ts_to_list
    # helper function below for conversion

    return denoised


def impute_missing_data(ts):
    """ Encodes missing data in time series as
    blanks for efficiency when reading files. 
    Uses Pandas library modules. """

    # fills NaN values with 0s
    ts.fillna(0)

    return ts


def impute_outliers(ts):
    """ Removes outlier data points from time
    series list. Uses scikit ML modules to
    search for outliers. """

    # removes all random numbers that lie in the lowest 15
    # percent quantile and the highest 85 percent quantile
    ts = ts[ts.between(ts.quantile(.15), ts.quantile(.85))]

    return ts


def longest_continuous_run(ts):
    """ Finds the longest amount of time in
    the time series list without any missing
    or blank data. Returns a time series. Uses
    scikit ML modules to search through list. """

    f = dict(Start=pd.Series.first_valid_index,
             Stop=pd.Series.last_valid_index,
             Stretch='count')

    agged = ts.values.groupby(ts.values.isnull().cumsum()).agg(f)
    agged.loc[agged.Stretch.idxmax(), ['Start', 'Stop']].values

    return agged


def clip(ts, starting_date, final_date):
    """ Removes parts of the time series that
    fall outside of the start date and end date. """

    # having issues with this because there are no
    # dates in the data sets he uploaded
    return ts.between_time(starting_date, final_date, axis='index')


def assign_time(ts, start, increment):
    """ Assign times with a sequence of readings, 
    beginning with start time and separating times
    by the increment value. """

    return "Not implemented yet"


def differences(ts):
    """ Returns a time series with magnitudes
    equivalent to the amount of space between
    consecutive elements in the original time
    series.  """

    return ts.diff()


def scaling(ts):
    """ Returns a time series whose magnitudes
    are scaled so resulting magnitudes range
    fall inside of [0,1] """

    values = ts.values
    values = values.reshape((len(values), 1))
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler = scaler.fit(values)
    normalized = scaler.transform(values)

    return normalized


def standardize(ts: list):
    """ Returns a time series whose mean
    is 0 and variance is 1. """

    return "Not implemented yet"


def logarithm(ts: list):
    """ Returns a time series whose elements are
    the logarithm of the original elements. """

    return "Not implemented yet"


def cubic_root(ts: list):
    """ Returns a time series whose
    elements are the cubic root of 
    each of the original elements. """

    return "Not implemented yet"


def split_data(ts: list, perc_training: float, perc_valid: float,
               perc_test: float):
    """ Returns a time series separated into training, 
    validation, and testing according to the specified
    percentages. """

    # ML data: test data set, training data set, split the CSV data
    # based on what percentages are passed in

    return "Not implemented yet"


def design_matrix(ts: list, input_index: int, output_index: int):
    """ Creates a forecasing model based on the input
    and output specified in input_index and output_index. 
    The output index indicated how many predictions 
    are necessary and their distance from each
    other. """

    return "Not implemented yet"


def ts2db(input_filename: str, perc_training: float,
          perc_valid: float, perc_test: float,
          input_index: int, output_index: int,
          output_file_name: str):
    """ Function reads an input file, splits data into
    training, validation, and testing according to
    percentages, and converts to a database in the
    form of an output file. """

    return "Not implemented yet"


def main():
    ts = read_file("../time_series_data/1_temperature_test.csv")
    denoised = denoise(ts)
    cleaned1 = impute_missing_data(denoised)
    cleaned2 = impute_outliers(cleaned1)
    # clipped = clip(cleaned2, 0, 4)
    diff = differences(cleaned2)
    scaled = scaling(diff)


if __name__ == '__main__':
    main()

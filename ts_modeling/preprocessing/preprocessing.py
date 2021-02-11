#!/usr/bin/env/python

"""
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis

Utility: preprocessing functions for reading data files
and preparing them for visualization.

Note: pandas, math, statsmodels, matplotlib, and
sklearn must be downloaded in order to use this
software.
"""

# import statements below
import math
import pandas as pd
import numpy as np
from random import random
from sklearn.preprocessing import *
import matplotlib.pyplot as plt
import datetime as dt

__authors__ = "Stephanie Schofield, Kyra Novitzky"
__version__ = "1.0.0"
__emails__ = "sschofie@cs.uoregon.edu, knovitzk@uoregon.edu"
__credits__ = "Ronny Fuentes, Alec Springel, Seth Tal"
__date__ = "01/22/2021"


def read_from_file(csv_input_fname: str):
    """ Reads a CSV file and converts it to a time series."""

    # reads the csv file
    # head = None to specify no header
    # index_col = 0 to show that first column contains index info
    # squeeze=True because we only have one data column and want a time series
    # this converts ts to a time series

    ts = pd.read_csv(csv_input_fname, header=None, squeeze=True)

    return ts


def write_to_file(ts, csv_output_fname: str):
    """ Writes a CSV file given a time series. """

    # given a time series ts, to_csv function writes
    # time series information to a CSV file named
    # csv_output_fname. if file does not exist it will
    # be created. returns ts, a time series

    ts.to_csv(csv_output_fname)

    return ts


def list_to_ts(ts_list):
    """ Converts list to a time series object. """

    # converts ts_list to a Series
    ts = pd.Series(ts_list)

    return ts


def ts_to_list(ts):
    """ Converts time series object to a list for
        visualization. """

    # converts time series object to list
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

    ts = ts_to_list(ts)
    clipped = list_to_ts(ts[starting_date: final_date + 1])

    return clipped


def assign_time(ts, start, increment):
    """ Assign times with a sequence of readings,
    beginning with start time and separating times
    by the increment value. """

    col = ts.columns[len(ts.columns) - 1]
    assigned = pd.DataFrama(columns=["Date", "Val"])
    for num in ts.index:
        assigned.loc[num] = ts.at[num, col]

    date_col = assigned.columns[0]
    date = start.split(sep="/")
    day = int(date[1])
    month = int(date[0])
    year = int(date[2])
    full_date = dt.datetime(year, month, day)

    for item in assigned.index:
        assigned.at[item, date_col] = full_date
        full_date += dt.timedelta(hours=increment)

    return assigned


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


def standardize(ts):
    """ Returns a time series whose mean
    is 0 and variance is 1. """

    values = ts.values
    values = values.reshape((len(values), 1))
    scaler = StandardScaler()
    scaler = scaler.fit(values)
    normalized = scaler.transform(values)

    return normalized


def logarithm(ts):
    """ Returns a time series whose elements are
    the logarithm of the original elements. """

    ts_list = ts_to_list(ts)
    for i in range(0, len(ts)):
        ts_list[i] = float(math.log(ts_list[i], 10))

    ts = list_to_ts(ts_list)

    return ts


def cubic_root(ts):
    """ Returns a time series whose
    elements are the cubic root of
    each of the original elements. """

    ts_list = ts_to_list(ts)
    for i in range(0, len(ts)):
        ts_list[i] = float(ts_list[i] ** (1/3))

    ts = list_to_ts(ts_list)

    return ts


def split_data(ts, perc_training: float, perc_valid: float,
               perc_test: float):
    """ Returns a time series separated into training,
    validation, and testing according to the specified
    percentages. """

    # kyra's code below -- need to test

    x_train, x_val, x_test = np.split(
        ts.sample(frac=1),
        [int(perc_training * len(ts)),
         int(1 - perc_test * len(ts))])

    return x_train, x_val, x_test


def design_matrix(ts_list: list, input_indices: list, rows: int, cols: int):
    """ Creates a forecasting model based on the time
    series data and previous index. The length of
    ts_list and input_indices must be the same in order
    for the matrix to be produced. """

    if len(ts_list) != len(input_indices):
        return "Length of time series and input indices must be equal."

    # convert list to time series
    ts = list_to_ts(ts_list)

    ts.index = input_indices
    temp = ts.to_numpy()
    matrix = temp.reshape(rows, cols)

    return matrix


def ts2db(input_filename: str, perc_training: float,
          perc_valid: float, perc_test: float,
          output_file_name: str):
    """ Function reads an input file, splits data into
    training, validation, and testing according to
    percentages, and converts to a database in the
    form of an output file. """

    ts = read_from_file(input_filename)
    train, validate, test = split_data(
        ts, perc_training, perc_valid, perc_test)
    db = pd.Series([train, validate, test])
    write_to_file(db, output_file_name)

    return db

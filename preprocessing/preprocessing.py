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
import sklearn
import matplotlib.pyplot as plt

__authors__ = "Stephanie Schofield"
__version__ = "1.0.0"
__emails__ = "sschofie@cs.uoregon.edu"
__credits__ = "Ronny Fuentes, Kyra Novitzky, Alec Springel, Seth Tal"
__date__ = "01/22/2021"


def read_file(csv_fname: str):
    """ Reads a CSV file and converts into readable format."""

    # reads the csv file and adds "temp_in_celsius" as column name
    tfile = pd.read_csv(csv_fname, names=["temp_in_celsius"])
    # renames index column to "day"
    tfile.index.name = "day"

    # fig, axs = plt.subplots(figsize=(12, 4))
    # tfile.groupby(tfile[0]).plot(kind='bar', rot=0, ax=axs)
    print(tfile.head())


def denoise(ts: list):
    """ Removes noise from times series. Takes in
    time series list, processes using modules and 
    moving median from Pandas library. """

    # add enumerators for tagging
    # might be another library that does this
    # want to write as little custom code as possible

    return "Not implemented yet"


def impute_missing_data(ts: list):
    """ Encodes missing data in time series as
    blanks for efficiency when reading files. 
    Uses Pandas library modules. """

    return "Not implemented yet"


def impute_outliers(ts: list):
    """ Removes outlier data points from time
    series list. Uses scikit ML modules to
    search for outliers. """

    return "Not implemented yet"


def longest_continuous_run(ts: list):
    """ Finds the longest amount of time in
    the time series list without any missing
    or blank data. Returns a time series. Uses
    scikit ML modules to search through list. """

    return "Not implemented yet"


def clip(ts: list, starting_date: tuple, final_date: tuple):
    """ Removes parts of the time series that
    fall outside of the start date and end date. """

    return "Not implemented yet"


def assign_time(ts: list, start: tuple, increment: int):
    """ Assign times with a sequence of readings, 
    beginning with start time and separating times
    by the increment value. """

    return "Not implemented yet"


def differences(ts: list):
    """ Returns a time series with magnitudes
    equivalent to the amount of space between
    consecutive elements in the original time
    series.  """

    return "Not implemented yet"


def scaling(ts: list):
    """ Returns a time series whose magnitudes
    are scaled so resulting magnitudes range
    fall inside of [0,1] """

    return "Not implemented yet"


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


read_file("../time_series_data/1_temperature_test.csv")

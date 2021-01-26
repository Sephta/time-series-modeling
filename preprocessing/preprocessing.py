#!/usr/bin/env/python

""" 
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis

Utility: preprocessing functions for reading data files
and preparing for visualization.

Note: pandas and sklearn must be downloaded in order to use this 
software. 
"""

# import statements below
import sys
import pandas
import sklearn

__authors__ = "Ronny Fuentes, Stephanie Schofield"
__version__ = "1.0.0"
__emails__ = "ronnyf@uoregon.edu, sschofie@cs.uoregon.edu"
__credits__ = "Kyra Novitzky, Alec Springel, Seth Tal"
__date__ = "01/22/2021"


def denoise(list: ts):
    """ Removes noise from times series. Takes in
    time series list, processes using modules and 
    moving median from Pandas library. """

    return "Not implemented yet"


def impute_missing_data(list: ts):
    """ Encodes missing data in time series as
    blanks for efficiency when reading files. 
    Uses Pandas library modules. """

    return "Not implemented yet"


def impute_outliers(list: ts):
    """ Removes outlier data points from time
    series list. Uses scikit ML modules to
    search for outliers. """

    return "Not implemented yet"


def longest_continuous_run(list: ts):
    """ Finds the longest amount of time in
    the time series list without any missing
    or blank data. Returns a time series. Uses
    scikit ML modules to search through list. """

    return "Not implemented yet"


def clip(list: ts, tuple: starting_date, tuple: final_date):
    """ Removes parts of the time series that
    fall outside of the start date and end date. """

    return "Not implemented yet"


def assign_time(list: ts, tuple: start, int: increment):
    """ Assign times with a sequence of readings, 
    beginning with start time and separating times
    by the increment value. """

    return "Not implemented yet"


def differences(list: ts):
    """ Returns a time series with magnitudes
    equivalent to the amount of space between
    consecutive elements in the original time
    series.  """

    return "Not implemented yet"


def scaling(list: ts):
    """ Returns a time series whose magnitudes
    are scaled so resulting magnitudes range
    fall inside of [0,1] """

    return "Not implemented yet"


def standardize(list: ts):
    """ Returns a time series whose mean
    is 0 and variance is 1. """

    return "Not implemented yet"


def logarithm(list: ts):
    """ Returns a time series whose elements are
    the logarithm of the original elements. """

    return "Not implemented yet"


def cubic_root(list: ts):
    """ Returns a time series whose
    elements are the cubic root of 
    each of the original elements. """

    return "Not implemented yet"


def split_data(list: ts, float: perc_training, float: perc_valid,
               float: perc_test):
    """ Returns a time series separated into training, 
    validation, and testing according to the specified
    percentages. """

    return "Not implemented yet"


def design_matrix(list: ts, int: input_index, int: output_index):
    """ Creates a forecasing model based on the input
    and output specified in input_index and output_index. 
    The output index indicated how many predictions 
    are necessary and their distance from each
    other. """

    return "Not implemented yet"


def ts2db(string: input_filename, float: perc_training,
          float: perc_valid, float: perc_test,
          int: input_index, int: output_index,
          string: output_file_name):
    """ Function reads an input file, splits data into
    training, validation, and testing according to
    percentages, and converts to a database in the
    form of an output file. """

    return "Not implemented yet"

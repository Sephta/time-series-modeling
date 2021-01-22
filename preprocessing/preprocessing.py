#!/usr/bin/env/python

""" 
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis

Utility: preprocessing functions for reading data files
and preparing for visualization.
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

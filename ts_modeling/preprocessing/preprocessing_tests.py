#!/usr/bin/env/python

"""
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis

Utility: Testing preprocessing functions.

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
import ts_modeling.preprocessing.preprocessing as pre

__authors__ = "Stephanie Schofield"
__version__ = "1.0.0"
__emails__ = "sschofie@cs.uoregon.edu, knovitzk@uoregon.edu"
__credits__ = "Ronny Fuentes, Alec Springel, Seth Tal"
__date__ = "02/10/2021"


def conversion_test(csv_input_fname):
    """ Prints contents of time series during
    conversion process to check that functions 
    are transforming time series to lists and back
    to a time series. """
    print()
    print()
    print(" ------------ CONVERSION TEST ------------ ")
    print()
    print()
    ts = pre.read_from_file(csv_input_fname)
    print(" ------------- TIME SERIES --------------- ")
    print(ts)
    print()
    print()
    ts_list = pre.ts_to_list(ts)
    print(" --------- TIME SERIES --> LIST ---------")
    print(ts_list)
    print()
    print()
    new_ts = pre.list_to_ts(ts_list)
    print("----------- LIST --> TIME SERIES ---------")
    print(new_ts)
    print()
    print()
    print("------------------------------------------")
    print()
    print()


def design_matrix_test(csv_input_fname):
    """ Testing design_matrix """

    ts = pre.read_from_file(csv_input_fname)
    ts_list = pre.ts_to_list(ts)
    indices = [x for x in range(0, 144)]
    pre.design_matrix(ts_list, indices, 4, 36)


def ts2db_test(csv_input_fname):
    """ Testing ts2db """

    pre.ts2db(csv_input_fname, 10.0, 20.0, 70.0, "output.txt")


def split_data_test(csv_input_fname):
    """ Testing split_data """

    time_series = pre.read_from_file(csv_input_fname)
    x, y, z = pre.split_date(time_series, 0.6, 0.2, 0.2)


def assign_time_test(csv_input_fname):
    """ Testing assign_time_test """

    ts = pre.read_from_file(csv_input_fname)
    pre.assign_time(ts, 0, 10)


def pipeline(csv_input_fname):
    """ Running preprocessing functions in 
    a pipeline for testing. """

    ts = pre.read_from_file(csv_input_fname)
    denoised = pre.denoise(ts)
    cleaned1 = pre.impute_missing_data(denoised)
    cleaned2 = pre.impute_outliers(cleaned1)
    # not working yet -- clipped = clip(cleaned2, 0, 4)
    diff = pre.differences(cleaned2)
    scaled = pre.scaling(diff)


def main():
    test_file = "Time Series Data/1_temperature_test.csv"

    # testing that conversion from time series object to
    # list and then back to time series object functions
    # are working correctly
    # commenting out conversion_test b/c lots of print statements
    # conversion_test(test_file)
    design_matrix_test(test_file)
    ts2db_test(test_file)
    pipeline(test_file)
    assign_time_test(test_file)


if __name__ == '__main__':
    main()

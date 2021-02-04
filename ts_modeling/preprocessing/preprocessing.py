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
import numpy

__authors__ = "Kyra Novitzky"
__version__ = "1.0.0"
__emails__ = "knovitzk@uoregon.edu"
__credits__ = "Alec Springel, Seth Tal, Ronny Fuentes, Stephanie Schofield"
__date__ = "02/03/2021"


def denoise(ts):
    """ Removes noise from times series. Takes in
    time series list, processes using modules and 
    moving median from Pandas library. """
    series = pandas.Series(ts) #converts the time series list into a Pandas Series
                               #which is just a 1D array capable of holding any data
    #print("Original series data:\n", series)

    denoised_series = series.rolling(len(ts), min_periods=1).median()   #converts series data points
                                                                        #into the median of the window.
                                                                        #With the max window being the
                                                                        #length of the data.
                                                                        #min_periods = min amount of data
                                                                        #required at a given series position.
    #print("Denoised series data:\n", denoised_series)
    denoised_list = denoised_series.values.tolist()                     #converts series values back into
                                                                        #list for visualization
    #print("Denoised list data\n", denoised_list)

"""
Use below code to test denoise. ts represents a list of time series data.
Don't forget to remove '#' from commented out print statement within
denoise function in order to visualize what is going on.
"""
"""
ts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
denoise(ts)
"""
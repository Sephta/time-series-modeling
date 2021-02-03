from numpy import genfromtxt
import numpy as np
import matplotlib
import seaborn  # How to represent statistical data
from matplotlib import pyplot as plt
import pandas as pd


def build_matrix(input_f):
    """
    read csv file, and throws all the data from the file
    into a list. Return value is a python list with all the
    numbers from a file.
    """
    # test points:   #1     #2    #3   #4
    # yellow
    # input_matrix = [[21.4, 60.4, 11.5, 28.4, 23.4], 40.8,
    #                 [23.2, 22.8, 22.7, 22.5, something],
    input_matrix = [[21.4, 60.4, 11.5, 28.4],
                    [23.2, 22.8, 22.7, 22.5],
                    [22.2, 22.3, 21.9, 21.9],
                    [18.4, 18.2, 18.1, 17.9]]

    # X = [[0., 0.], [1., 1.]]
    # y = [0, 1]  # the actual output.

    coordinates = []
    with open(input_f) as f:
        f.readline()  # skips the garbage at the beginning of the file
        for item in f:
            coordinates.append(item.rstrip('\n'))

    mx = np.array(input_matrix)
    # width is 4 (4 rows) ?
    return mx


print(build_matrix('Time Series Data/1_temperature_test.csv'))

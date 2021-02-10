#!/usr/bin/env/python

"""
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis

Utility: Forecasting functions including mlp_model, fit and forecast.

Note: numpy and sklearn must be downloaded in order to use
this software.
"""

__authors__ = "Kyra Novitzky"
__version__ = "1.1.0"
__emails__ = "knovitzk@uoregon.edu"
__credits__ = "Alec Springel, Seth Tal, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/29/2021"

import sklearn
from sklearn.neural_network import MLPClassifier  # For mlp model
from numpy import array  # For split function
import numpy


class MlpModel:
    def __init__(self, data, num_steps):
        # The literal mlp model
        self.mlp = MLPClassifier(solver='lbfgs', max_iter=10000)
        self.data = data  # The data being used (time series files)
        # The amount of data desired in one sample
        self.num_time_steps = num_steps
        self.X = list()  # Input Matrix
        self.y = list()  # Output Matrix
        self.split_data()  # Calling split_data() which is required
        # to use fit and forecast

    def split_data(self):
        """
        This function takes a time series as input, in the form of a
        univariate sequence (list), and splits it into groups containing the
        number of steps specified. The output is a single step per
        sample input.
        Note: This function must be used in order to implement fit and forecast

        Ex:
        time_series = [10, 20, 30, 40, 50, 60]

        #Again, 3 represents the amount of data points for in a row of input
        X, y = split_data(time_series, 3)
        for i in range(len(X)):
            print(X[i], y[i])

        Output:
        [10, 20, 30] 40     1 sample with 3 input steps and 1 output step
        [20, 30, 40] 50     [10, 20, 30] = sample with 3 input steps
        [30, 40, 50] 60     40 = output which is a single step

        Behind the scenes:
        #This is a multi-dimensional matrix, hence X
        X = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]
        #This is a 1D matrix, hence y
        y = [40, 50, 60]
        """
        # X, y = list(), list()

        for i in range(len(self.data)):
            # find the end of this pattern
            end_ix = i + self.num_time_steps
            # check if we are beyond the sequence
            if end_ix > len(self.data) - 1:
                break
            # gather input and output parts of the pattern
            seq_x = self.data[i: end_ix]
            seq_y = self.data[end_ix]
            self.X.append(seq_x)
            self.y.append(seq_y)
        return array(self.X), array(self.y)

    def forecast(self, input_for_prediction):
        """
        This function produces a forecase for the time series's
        current state, x.

        input_for_prediction is the sequence that we want to predict the next
        output for.

        Ex:
        input_array = [40, 50, 60]
        forecast(input_array)

        Output:
        [70]            This is because we are predicting what the
                        next number would be in the input_array.
                        Since the other integers are increasing by
                        10, the next number in the sequence will
                        most likely be 70
        """
        input_for_prediction = array(
            input_for_prediction)  # Changes list into an array
        # Ex: [40, 50, 60] ---> [40 50 60]

        input_for_prediction = input_for_prediction.reshape(
            (1, len(input_for_prediction)))

        # Reshapes the array into a new array consisting of that array
        # Ex: [40 50 60] ---> [[40 50 60]]
        # Note: still unsure of what the shape (or array being passed to
        # predict) needs to be in order to function correctly
        # I think array must be the same dimension as y

        return self.mlp.predict(input_for_prediction)

    # make sure forecast returns a list

    def fitt(self):
        new_y = array(self.y, dtype="|S6")
        # needs to use above if time series data is floats.
        # can use below if time series data is just just ints.
        # new_y = array(self.y)
        print(new_y)
        self.mlp.fit(self.X, new_y)

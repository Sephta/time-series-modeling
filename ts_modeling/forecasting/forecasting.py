#!/usr/bin/env/python

""" 
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis

Utility: Forecasting functions including mlp_model, fit and forecast.

Note: numpy and sklearn must be downloaded in order to use this 
software. 
"""

__authors__ = "Kyra Novitzky"
__version__ = "1.0.0"
__emails__ = "knovitzk@uoregon.edu"
__credits__ = "Alec Springel, Seth Tal, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/29/2021"

import sklearn
from sklearn.neural_network import MLPClassifier #For mlp model
from numpy import array #For split function

class mlp_model:
    def __init__(self, data, num_steps):
        self.mlp = MLPClassifier(solver='lbfgs', max_iter=10000) #The literal mlp model
        self.data = data                                #The data being used (time series files)
        self.num_time_steps = num_steps                 #The amount of data desired in one sample
        self.X = list()                                 #Input Matrix
        self.y = list()                                 #Output Matrix
        self.split_data()                               #Calling split_data() which is required
                                                        #to use fit and forecast

    def split_data(self):
        """
        This function takes a time series as input, in the form of a
        univariate sequence (list), and splits it into groups containing the
        number of steps specified. The output is a single step per
        sample input.
        Note: This function must be used in order to implement fit and forecast

        Ex:
        time_series = [10, 20, 30, 40, 50, 60]

        X, y = split_data(time_series, 3)   #Again, 3 represents the amount of data points for in a row of input
        for i in range(len(X)):
            print(X[i], y[i])

        Output:
        [10, 20, 30] 40         This line is 1 sample with 3 input steps and 1 output step
        [20, 30, 40] 50         [10, 20, 30] = sample with 3 input steps
        [30, 40, 50] 60         40 = output which is a single step

        Behind the scenes:
        X = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]      #This is a multi-dimensional matrix, hence X
        y = [40, 50, 60]                                    #This is a 1D matrix, hence y
        """
        #X, y = list(), list()
        for i in range(len(self.data)):
            # find the end of this pattern
            end_ix = i + self.num_time_steps
            # check if we are beyond the sequence
            if end_ix > len(self.data)-1:
                break
            # gather input and output parts of the pattern
            seq_x = self.data[i : end_ix]
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
        input_for_prediction = array(input_for_prediction)  #Changes list into an array 
                                                            #Ex: [40, 50, 60] ---> [40 50 60]

        input_for_prediction = input_for_prediction.reshape((1, len(input_for_prediction)))

        # Reshapes the array into a new array consisting of that array
        # Ex: [40 50 60] ---> [[40 50 60]]
        # Note: still unsure of what the shape (or array being passed to predict) 
        # needs to be in order to function correctly
        # I think array must be the same dimension as y

        return self.mlp.predict(input_for_prediction)

    # make sure forecast returns a list

"""
Below is an example on how to use the object mlp_model along with it's
functionalities. Can remove quotes to test.
"""

"""
print("\n")

time_series = [10, 20, 30, 40, 50, 60, 70, 80, 90]   #Represents time series data in form of list

steps = 3                                            #Represents the number of data points
                                                     #desired in a sample when splitting data.
                                                     #See split_data comment for further details.
                                                     #Going to ask Flores what this should be for
                                                     #differing TS data.

example = mlp_model(time_series, steps)              #Creates the mlp_model and assigns it to example

for i in range(len(example.X)):                      #Printing the output of what split_data() did to original data
    print(example.X[i], example.y[i])

example.mlp.fit(example.X, example.y)                #Fitting data (must do this before forecasting)
                                                     #parameters will always be example.X and example.y

input = [20, 30, 40]

print("\n")

print("Forecast for",                                #Prints forecast for an inputted sequence
      input, ":", example.forecast(input))

print("\n")
"""
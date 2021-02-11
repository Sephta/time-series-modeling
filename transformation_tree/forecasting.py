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
__version__ = "1.2.1"
__emails__ = "knovitzk@uoregon.edu"
__credits__ = "Alec Springel, Seth Tal, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/29/2021"

import sklearn
from sklearn.neural_network import MLPClassifier  # For mlp model
from numpy import array  # For split function


class MlpModel:
    def __init__(self, input_dimension, output_dimension):
        # The literal mlp model
        self.mlp = MLPClassifier(solver='lbfgs', max_iter=10000)
        self.input_dimension = input_dimension
        self.output_dimension = output_dimension

    def forecast(self, input_for_prediction):
        """
        This function produces a forecase for the time series's
        current state, x.

        input_for_prediction is the sequence that we want to predict the next
        output for.

        Ex:
        input = [40, 50, 60]
        forecast(input_array)

        Output:
        [70]            This is because we are predicting what the
                        next number would be in the input_array.
                        Since the other integers are increasing by
                        10, the next number in the sequence will
                        most likely be 70
        """
        return self.mlp.predict(input_for_prediction)

    def fit(self, train_x, train_y):
        """Trains the mlp model for prediction."""
        self.mlp.fit(train_x, train_y)

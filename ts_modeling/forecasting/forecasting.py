#!/usr/bin/env/python

""" 
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis

Utility: forecasting functions

Note: pandas and sklearn must be downloaded in order to use this 
software. 
"""

# import statements below
# import sys
# import pandas
import sklearn

__authors__ = "Kyra Novitzky"
__version__ = "1.0.0"
__emails__ = "ronnyf@uoregon.edu, sschofie@cs.uoregon.edu"
__credits__ = "Alec Springel, Seth Tal, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/22/2021"

from sklearn.neural_network import MLPClassifier

class Mlp:
    def __init__(self, input_dimension, output_dimension):
        self.mlp = MLPClassifier(solver='lbfgs', alpha=1e-5,
                                 hidden_layer_sizes=(5, 2), random_state=1)
        self.input_dim = input_dimension
        self.output_dim = output_dimension

    def mlp_model(input_dimension, output_dimension):
        """
        This function defines a Multi-Layer Perceptron model. 
        """
        return

example = Mlp(5, 3)
print("example's input dimension is: ", example.input_dim)
print("example's output dimension is: ", example.output_dim)










X = [[0., 0.], [1., 1.]]

"""
X = [[0., 0.]]
"""

y = [1, 7]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)

print(clf.fit(X, y))

print(clf.predict([[2., 2.], [-1., -2.]]))


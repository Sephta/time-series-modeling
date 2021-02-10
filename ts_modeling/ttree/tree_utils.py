"""Helper functions for tree backend.

This module contains helper functions to load TTree and Pipeline objects

Functions:
    load_tree
    load_pipeline
    copy_path

"""
import pickle

__authors__ = "Alec Springel"
__version__ = "1.0.0"
__emails__ = "aspring6@uoregon.edu, stal@uoregon.edu"
__credits__ = "Kyra Novitzky, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/24/2021"


def load_tree(file: str):
    """Loads tree as python object from specified file path"""
    with open(file, 'rb') as handle:
        tree = pickle.load(handle)
    return tree


def load_pipeline(file_path: str):
    """Loads pipeline from filepath. Expects pickle file..."""
    with open(file_path, 'rb') as file:
        pipeline = pickle.load(file)
    if pipeline:
        return pipeline
    else:
        raise Exception("ERROR: encountered error loading pipeline from file path: \"" + file_path + "\"")


def copy_path(path):
    copy = []
    for node in path:
        copy.append(node.copy())
    return copy

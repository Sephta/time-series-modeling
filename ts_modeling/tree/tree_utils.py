"""
Utility: Helper functions for tree backend.
"""
import pickle
from tree import TTree

__authors__ = "Alec Springel"
__version__ = "1.0.0"
__emails__ = "aspring6@uoregon.edu, stal@uoregon.edu"
__credits__ = "Kyra Novitzky, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/24/2021"



def load_tree(file: str) -> TTree:
    """Loads tree as python object from specified file path"""
    with open(file, 'rb') as handle:
        tree = pickle.load(handle)
    return tree

def copy_path(path):
    copy = []
    for node in path:
        copy.append(node.copy())
    return copy

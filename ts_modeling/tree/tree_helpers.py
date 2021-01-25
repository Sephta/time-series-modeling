"""
Utility: Helper functions for tree backend.
"""

__authors__ = "Alec Springel"
__version__ = "1.0.0"
__emails__ = "aspring6@uoregon.edu, stal@uoregon.edu"
__credits__ = "Kyra Novitzky, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/24/2021"


def copy_nodes(nodes):
    copy = []
    for node in nodes:
        copy.append(node.copy())
    return copy

"""
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis
Utility: Tree backend for storing all potential pipelines.
"""

# import statements below
from anytree import NodeMixin, RenderTree, render
from typing import List, Callable

__authors__ = "Alec Springel"
__version__ = "1.0.0"
__emails__ = "aspring6@uoregon.edu"
__credits__ = "Kyra Novitzky, Seth Tal, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/23/2021"


class Node(NodeMixin):
    def __init__(self, name: str, function: Callable, parent=None):
        self.name = name
        self.function = function
        # Parents/children are dynamically generat ed by checking input/output
        self.parent = parent

    def set_parent(self, parent):
        self.parent = parent
        return self.parent


class TTree():
    def __init__(self, name: str, path_to_data: str):
        self.name = name
        self.path_to_data = path_to_data
        self.root = Node("Data", None, None)

    def print(self):
        """Prints a visual representation of the tree"""
        for pre, fill, node in RenderTree(self.root):
            treestr = u"%s%s" % (pre, node.name)
            print(treestr.ljust(8))

    def add_path(self, target: Node, path: [Node]):
        """Adds a path beginning at the target node, iterating through
        the array and ending at the last element in array (leaf)"""
        path[0].set_parent(target)
        for i in range(1, len(path)):
            path[i].set_parent(path[i-1])

"""
Tree tests: testing add_path_** methods

USE: 'pytest' in command line to execute
"""
import pytest
import os
import sys
import testops
# Needed to import from parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# IGNORE IMPORT NOT AT TOP OF FILE
from tree import TTree, Node


# TESTS
def test_add_path():
    tree = TTree("test", Node(testops.root))
    path = [Node(testops.op1), Node(testops.op2), Node(testops.op3)]
    tree.add_newpath(tree.root, path)
    print(tree)
    # Check if each node in tree has 1 child and all nodes were added to tree
    current = tree.root
    num_nodes = 1
    while current.children:
        assert len(current.children) == 1
        current = current.children[0]
        num_nodes += 1
    assert num_nodes == 4


def test_add_path_byid():
    tree = TTree("test", Node(testops.root))
    path = [Node(testops.op1), Node(testops.op2), Node(testops.op3)]
    tree.add_newpath_byid(0, path)
    print(tree)
    # Check if each node in tree has 1 child and all nodes were added to tree
    current = tree.root
    num_nodes = 1
    while current.children:
        assert len(current.children) == 1
        current = current.children[0]
        num_nodes += 1
    assert num_nodes == 4

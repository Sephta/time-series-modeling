"""
Tree tests: testing TTree helper methods

USE: 'pytest' in command line to execute
"""
import pytest
import os
import sys
from .testops import op1, op2, op3, root
# Needed to import from parent directory
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# IGNORE IMPORT NOT AT TOP OF FILE
from ..tree import TTree, Node, Pipeline


# TESTS
def test_reparent():
    tree = TTree("test", Node(root))
    n1 = Node(op1)
    # Add n1 and n2 to root as children
    tree.add_nodes(tree.root, n1)
    # Add n2 with children to parent
    n2 = Node(op3)
    path = [n2, Node(op1), Node(op2)]
    tree.add_newpath(tree.root, path)
    print(tree)
    # set n1 as new parent of n2. n2 should take its children with it
    tree.reparent_node(n1, n2)
    print(tree)
    # Check that n2 maintained its path. Check that each child is the same.
    for i in range(len(path) - 1):
        child = path[i].children[0]
        assert child and path[i].id == child.id - 1
    assert len(n1.children) == 1


def test_pipeline_print():
    pre_pipeline = [root, op1, op2, op3]

    pipe = Pipeline(operators=pre_pipeline)
    print(pipe)


test_pipeline_print()
test_reparent()

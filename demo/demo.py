from time_series_modeling.ts_modeling.tree import *


def root():
    print("hello world")


test = Node(root)

tree = TTree("Test", test)

print(tree)

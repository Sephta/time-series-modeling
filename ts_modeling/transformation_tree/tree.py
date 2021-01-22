""" Seth Tal
 * 01.21.21
 * Transformation Tree backend
"""


class Node:
    def __init__(self, key, children=None):
        self.key = key
        self.children = children


class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, newNode: Node):
        if self.root is None:
            self.root = newNode

    def printTree(self):
        current = self.root
        while(current is not None):
            print("Node: " + str(current.key))
            current = current.children
            if current is not None:
                for i in range(len(current)):
                    if current[i] is not None:
                        print("Child: " + str(current[i].key))
                current = None


def test():
    T_test = Tree()
    n1 = Node(2)
    n2 = Node(3)
    N_test = Node(1, [n1, n2])
    T_test.addNode(N_test)
    T_test.printTree()


test()

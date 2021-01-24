from tree import Node, TTree
from anytree import NodeMixin, RenderTree, render


def operator():
    return "Operator Function"


def generate_tree():
    tree = TTree("test", "C:/Users/aspri/Documents")
    a = Node('a', operator)
    b = Node('b', operator)
    c = Node('c', operator)

    tree.add_path(tree.root, [a, b, c])

    tree.add_path(a, [Node('a', operator), Node(
        'b', operator), Node('c', operator)])

    tree.add_path(a, [Node('a', operator), Node(
        'b', operator), Node('c', operator)])

    tree.print()


generate_tree()

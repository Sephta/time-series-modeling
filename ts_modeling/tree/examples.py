from tree import Node
from anytree import NodeMixin, RenderTree, render


def operator():
    return "Operator Function"


def create_nodes():
    """Returns root node for rendering"""
    testfun = operator
    a = Node('a', testfun, None, None)
    b = Node('b', testfun, None, None, parent=a)
    return a


def quick_render():
    root = create_nodes()
    print(RenderTree(root, style=render.DoubleStyle))


def verbose_render():
    root = create_nodes()
    for pre, fill, node in RenderTree(root):
        treestr = u"%s%s" % (pre, node.name)
        print(treestr.ljust(8), node.inType, node.outType, node.function())


verbose_render()
# quick_render()

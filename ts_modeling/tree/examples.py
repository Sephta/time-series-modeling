from tree import Node, TTree
from anytree import NodeMixin, RenderTree, render


def operator():
    return "Operator Function"


def denoise():
    return "Operator Function"


def generate_tree():
    rootNode = Node(operator)
    tree = TTree("test", rootNode)
    a = Node(operator)
    b = Node(operator)
    c = Node(operator)
    denoise_op2 = Node(operator)
    denoise_op1 = Node(operator)

    # tree.add_path(tree.root, [a, b, c])

    tree.add_path(tree.root,
                  [a,
                   Node(denoise),
                   Node(operator),
                   Node(denoise)])

    tree.add_path_byname("operator", [Node(denoise), Node(denoise)])
    # Takes non-list of Nodes

    # tree.add_path("d")

    # tree.add_path_byid(3, Node('a', operator))
    # tree.add_nodes(SOME_NODE_ID, [nodes are here])

    # tree.add_path(a, [Node('a', operator), Node(
    #     'b', operator), Node('c', operator)])

    tree.print(id=True)


generate_tree()

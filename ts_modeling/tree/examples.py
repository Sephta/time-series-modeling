from tree import Node, TTree
from anytree import NodeMixin, RenderTree, render


def root():
    return "root"


def _a():
    return "Operator Function"

def b():
    return "Operator Function"


def generate_tree():
    rootNode = Node(root)
    tree = TTree("test", rootNode)
    a = Node(_a)
    # b = Node(operator)
    # c = Node(operator)
    # denoise_op2 = Node(operator)
    # denoise_op1 = Node(operator)

    # tree.add_path(tree.root, [a, b, c])

    tree.add_newpath(tree.root,
                  [a,
                   Node(b),
                   Node(b),
                   Node(b)])

    tree.add_newpath(rootNode, Node(b))
    
    # print(a.get_id())

    # tree.add_newpath_byid(5, a)
    newA = Node(_a)
    tree.add_newpath_byid(5, newA)

    # print(a.get_id())

    # rtee.reparent(thingToReparent, thingToParentOnto)

    # tree.add_path_byname("operator", [Node(denoise), Node(denoise)])
    # tree.add_path_byid(0, [Node(denoise), Node(denoise)])
    # Takes non-list of Nodes

    # tree.add_path("d")

    # tree.add_path_byid(3, Node('a', operator))
    # tree.add_nodes(SOME_NODE_ID, [nodes are here])

    # tree.add_path(a, [Node('a', operator), Node(
    #     'b', operator), Node('c', operator)])

    tree.print(id=True)


generate_tree()

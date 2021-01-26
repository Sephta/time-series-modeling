from tree import Node, TTree
from anytree import NodeMixin, RenderTree, render
import pickle

""" Operator test functions
    * root : currently empty root node of a tree
    * _a   : does nothing currently
    * _b   : does nothing currently
"""


def root():
    return "Executing Operator root"


def _a():
    return "Executing Operator a"


def _b():
    return "Executing Operator b"


""" Test functions
    * literally just here to test certain types of functionality
"""


def generate_tree_test():
    rootNode = Node(root)
    tree = TTree("test", rootNode)
    a = Node(_a)
    b = Node(_b)

    # print('\n')
    # print(rootNode.children)
    # print('\n')

    tree.add_node(rootNode, a)
    tree.add_node(rootNode, b)

    tree.print_nodes_as_list()

    tree.print_tree(id=True)


def saving_tree_test():
    # For now user should start by creating a root node
    root_node = Node(root)

    # Maybe the user wants to create more nodes to add to the tree
    a_node = Node(_a)
    b_node = Node(_b)

    # Then user should create a tree and initialize it with a root node
    tree_to_save = TTree("root", root_node)

    # Then add nodes to the tree
    tree_to_save.add_node(root_node, a_node)
    tree_to_save.add_node(root_node, b_node)

    """ Tree in this example looks like this...
    *    root (0)
    *    ├── _a (1)
    *    └── _b (2)
    """

    print('\n')
    print("Confirm that tree matches example code:")
    tree_to_save.print_tree(True)
    print('\n')

    from anytree.exporter import JsonExporter

    # The default lambda expression tells json what the default value of an objects stuff should
    # be if the value cannot be serialized
    js_exporter = JsonExporter(
        indent=2, sort_keys=True, default=lambda o: '<not serializable>')

    with open("./ts_modeling/saved_trees/tree_to_save.json", 'w') as js_file:
        js_exporter.write(tree_to_save.root, js_file)
        print("Here is the json formatting:")
        print(js_exporter.export(tree_to_save.root))
        print('\n')

def testpickle():
    # For now user should start by creating a root node
    root_node = Node(root)

    # Maybe the user wants to create more nodes to add to the tree
    a_node = Node(_a)
    b_node = Node(_b)

    # Then user should create a tree and initialize it with a root node
    tree_to_save = TTree("root", root_node)
    tree_to_save.add_node(root_node, a_node)
    tree_to_save.add_node(root_node, b_node)

    with open("./ts_modeling/saved_trees/test_pickle.pickle", 'wb') as handle:
        pickle.dump(tree_to_save, handle)

    del a_node

    with open("./ts_modeling/saved_trees/test_pickle.pickle", 'rb') as handle:
        tree = pickle.load(handle)

    tree.print_tree(id=True)
    print(tree.root.function())


# generate_tree_test()
# saving_tree_test()
testpickle()

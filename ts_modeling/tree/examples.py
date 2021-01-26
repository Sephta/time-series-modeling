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

def test_func():
        return "Hello World"


""" Test functions
    * literally just here to test certain types of functionality
"""


def generate_tree_test():
    rootNode = Node(root)
    tree = TTree("test", rootNode)
    a = Node(_a)
    b = Node(_b)
    c = Node(_b)

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

def pickle_test():
    # For now user should start by creating a root node
    root_node = Node(root)

    # Maybe the user wants to create more nodes to add to the tree
    a_node = Node(_a)
    b_node = Node(_b)

    # Then user should create a tree and initialize it with a root node
    tree_to_save = TTree("root", root_node)
    tree_to_save.add_node(root_node, a_node)
    tree_to_save.add_node(root_node, b_node)

    # tests if pickle will serialize locally scoped functions
    # (it doesn't)
    def test_func2():
        return "hello world 2"
    
    # tests to see if pickle will serialize the function 
    # contained in the class "Test_func_class"
    test_func3 = Test_func_class()
    
    test_func_node = Node(test_func)
    # test_func2_node = Node(test_func2)
    # test_func3_node = Node(test_func3.test_func)
    
    
    tree_to_save.add_node(root_node, test_func_node)
    # tree_to_save.add_node(root_node, test_func2_node)
    # tree_to_save.add_node(root_node, test_func3_node)

    # print tree before saving to pickle file
    tree_to_save.print_tree(id=True)

    # location of the pickle file to save/load from
    pickle_file_location = "./ts_modeling/saved_trees/test_pickle.pickle"

    # saves tree object to file located at specified string
    tree_to_save.save(pickle_file_location)

    from tree import load_tree

    # loads tree object from pickle file
    loaded_tree = load_tree(pickle_file_location)
    
    # print loaded tree to see if 'tree_to_save' matches
    loaded_tree.print_tree(id=True)


class Test_func_class():

    def __init__(self):
        pass

    def test_func(self):
        return "Hello World"


# generate_tree_test()
# saving_tree_test()
pickle_test()

from tree import Node, TTree
from anytree import NodeMixin, RenderTree, render

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
    # b = Node(operator)
    # c = Node(operator)
    # denoise_op2 = Node(operator)
    # denoise_op1 = Node(operator)

    # tree.add_path(tree.root, [a, b, c])

    tree.add_newpath(tree.root,
                  [a,
                   Node(_b),
                   Node(_b),
                   Node(_b)])

    tree.add_newpath(rootNode, Node(_b))
    
    # print(a.get_id())

    # tree.add_newpath_byid(5, a)
    newA = Node(_a)
    tree.add_newpath_byid(5, newA)

    tree.print(id=True)

def saving_tree_test():
    # For now user should start by creating a root node
    root_node = Node(root)
    
    # Maybe the user wants to create more nodes to add to the tree
    a_node = Node(_a)
    b_node = Node(_b)

    # Then user should create a tree and initialize it with a root node
    tree_to_save = TTree("root", root_node)

    # Then add nodes to the tree
    tree_to_save.add_newpath(root_node, [a_node])
    tree_to_save.add_newpath(root_node, [b_node])
    
    """ Tree in this example looks like this...
    *    root (0)
    *    ├── _a (1)
    *    └── _b (2)
    """

    print('\n')
    print("Confirm that tree matches example code:")
    tree_to_save.print(True)
    print('\n')

    from anytree.exporter import JsonExporter

    js_exporter = JsonExporter(indent=2, sort_keys=True, default=lambda o: '<not serializable>')

    with open("./ts_modeling/saved_trees/tree_to_save.json", 'w') as js_file:
        js_exporter.write(tree_to_save.root, js_file)
        print("Here is the json formatting:")
        print(js_exporter.export(tree_to_save.root))
        print('\n')


# generate_tree_test()
saving_tree_test()

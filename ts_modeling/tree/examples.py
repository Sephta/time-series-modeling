from tree_utils import load_tree
from tree import *
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

class Test_func_class():

    def __init__(self):
        pass

    def test_func(self):
        return "Hello World"


""" Test functions
    * literally just here to test certain types of functionality
"""

#region Generate_tree_test()
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
#endregion

#region Saving_tree_test()
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

    # The default lambda expression tells json what the default value of an
    # objects stuff should be if the value cannot be serialized
    js_exporter = JsonExporter(
        indent=2, sort_keys=True, default=lambda o: '<not serializable>')

    with open("./ts_modeling/saved_trees/tree_to_save.json", 'w') as js_file:
        js_exporter.write(tree_to_save.root, js_file)
        print("Here is the json formatting:")
        print(js_exporter.export(tree_to_save.root))
        print('\n')
#endregion

#region Pickle_test()
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

    from tree_utils import load_tree

    # loads tree object from pickle file
    loaded_tree = load_tree(pickle_file_location)
    
    # print loaded tree to see if 'tree_to_save' matches
    loaded_tree.print_tree(id=True)
#endregion

#region Pipeline_test()
def test1():
    return "hello world (test 1), "

def test2(val: str):
    return (val + " test2 added", 1)

def test3(val):
    return val[0] + ", " + "test3 added, "

def test4(val: str):
    return (val + " this is TEST " + str(4), 4)


def pipeline_test():
    rootNode = Node(test1)
    a = Node(test2)
    b = Node(test3)
    c = Node(test4)

    pipeline = [rootNode, a, b, c]

    for i in range(len(pipeline)):
        if(i == 0):
            result = pipeline[i].function()
        else:
            result = pipeline[i].function(result)

    print(result[0])
#endregion

#region Test_pipeline_class()
def _preProcess():
    arr = [1, 2, 3, 4, 5, 6]
    print("op1...")
    print("Array to process: " + str(arr))
    return arr

def _denoise(arr: []):
    print("")
    print("op2...")
    result = [a*2 for a in arr]
    print("Array after \"denoising: \"" + str(result))
    return (result, "denoised")

def _scale(denoise_tuple):
    print("")
    print("op3...")
    result = [b**2 for b in denoise_tuple[0]]
    print("Array after \"scaling\": " + str(result))
    return (result, denoise_tuple[1] + ", scaled")

def _plot(scale_tuple):
    print("")
    print("op4...")
    print("Here is the data that was passed through the pipeline:")
    print(str(scale_tuple[0]))
    print(scale_tuple[1])

def Test_pipeline_class():
    print("")

    # Root of the tree
    rootNode = Node(root)

    # The tree itself
    tree = TTree("root", rootNode)

    # Tree nodes
    opA = Node(_preProcess)
    opB = Node(_denoise)
    opC = Node(_scale)
    opD = Node(_plot)

    tree.add_node(rootNode, opA)
    tree.add_node(opA, opB)
    tree.add_node(opB, opC)
    tree.add_node(opC, opD)

    print("TREE:")
    tree.print_tree()

    # TEST 1 =============================================================
    pre_pipeline = [opA.function, opB.function, opC.function, opD.function]

    pipeline_test1 = Pipeline(None, pre_pipeline)

    print("\nTest 1 { build test 1 }")
    pipeline_test1.print()
    # ====================================================================

    # TEST 2 =============================================================
    pipeline_test2 = Pipeline(opD, None)

    print("\nTest 2 { build test 2 }")
    pipeline_test2.print()
    # ====================================================================

    # TEST 3 =============================================================
    pipeline_test3 = Pipeline(opB, None)

    print("\nTest 3 { build test 3 }")
    pipeline_test3.print()
    # ====================================================================

    # TEST 4 =============================================================
    pipeline_test4 = Pipeline(None, pre_pipeline)

    print("\nTest 4 { pipeline execution }")
    pipeline_test4.execute()
    # ====================================================================

    # TEST 5 =============================================================
    print("\nTest 5 { pickling }")
    print("")
    print("Pipeline pre save...")
    pipeline_test5 = Pipeline(None, pre_pipeline)
    pipeline_test5.print()
    print("")

    pipeline_test5.save("./ts_modeling/saved_pipelines/pipe_test.pickle")

    from tree_utils import load_pipeline
    loaded_pipeline = load_pipeline("./ts_modeling/saved_pipelines/pipe_test.pickle")

    print("Pipeline after load...")
    loaded_pipeline.print()
    print("")

    print("Testing loaded pipeline execution...")
    loaded_pipeline.execute()
    # ====================================================================

    # TEST 6 =============================================================
    print("\nTest 6 { TTree.get_pipelines() }")
    print("")
    opA_2 = Node(_preProcess)
    opB_2 = Node(_denoise)
    opC_2 = Node(_scale)
    opD_2 = Node(_plot)

    opE = Node(_scale)
    opF = Node(_plot)

    tree.add_node(rootNode, opA_2)
    tree.add_node(opA_2, opB_2)
    tree.add_node(opB_2, opC_2)
    tree.add_node(opC_2, opD_2)
    tree.add_node(opB_2, opE)
    tree.add_node(opE, opF)

    print("Tree to test:")
    tree.print_tree()

    pipeline_list = tree.get_pipelines()
    
    for i in range(len(pipeline_list)):
        print("printing pipeline (" + str(i) + ")")
        pipeline_list[i].print()
    # ====================================================================

    # TEST 7 =============================================================
    print("\nTest 7 { TTree.generate_pipeline() }")
    print("")

    pipeline_test7 = tree.generate_pipeline(opB)
    pipeline_test7.print()

    # Uncomment the two lines bellow to test if proper exception is raised
    # opZ = Node(_preProcess)
    # pipeline_test7_pt2 = tree.generate_pipeline(opZ)

    # Uncomment line bellow to test if proper "byid" exception raised
    # pipeline_test7_pt3 = tree.generate_pipeline_byid(999)

    # ====================================================================

    print("")

#endregion


# generate_tree_test()
# saving_tree_test()
# pickle_test()
# pipeline_test()
Test_pipeline_class()

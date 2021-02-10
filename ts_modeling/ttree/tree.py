"""Tree backend for storing all potential pipelines.

This module contains the class definitions for Node, TTree, and Pipeline.

Classes:
    Node
    TTree
    Pipeline

.. Source Code:
    https://github.com/Sephta/time-series-modeling

"""
# region Imports
from __future__ import annotations
from anytree import NodeMixin, RenderTree, render, PostOrderIter
from typing import List, Callable, Union
from .tree_utils import copy_path
import pickle
# endregion

# region Module Meta data
__authors__ = "Alec Springel, Seth Tal"
__version__ = "1.0.0"
__emails__ = "aspring6@uoregon.edu, stal@uoregon.edu"
__credits__ = "Kyra Novitzky, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/23/2021"
# endregion


# region Node Class
class Node(NodeMixin):
    """Node for use in TTree class. Child class of NodeMixin from anytree.

    Attributes:
        name (str): name of this node
        function (Callable): reference to callable stored in this node
        parent (Node): reference to parent node of this node
        id (int): runtime id of this node
        children ([Node]): references to children of this node

    Args:
        function (Callable): function being stored in this Node
        parent (Node, optional): reference to node to set as parent
        children ([Node], optional): List of nodes to set as children
    """

    def __init__(self, function: Callable, parent: Node = None,
                 children: [Node] = None):
        self.name = function.__name__
        self.function = function
        self.parent = parent
        self.id = None  # Private
        if children is not None:
            self.children = children

    def __repr__(self):
        """__repr__ allows us to define the default string representation
        of this class"""
        return 'Operator: {}'.format(self.name)

    def set_id(self, id):
        """Used within the Node class. Should not be used outside of class"""
        self.id = id

    def get_id(self):
        """Returns id of this node"""
        return self.id

    def set_parent(self, parent):
        """Sets the parent of this Node"""
        self.parent = parent
        return self.parent

    def get_parent(self):
        """Returns the parent Node of this Node"""
        return self.parent

    def set_children(self, children):
        """Sets the children of this Node"""
        self.children = children

    def get_children(self):
        """Returns children of this Node as List"""
        return self.children

    def copy(self) -> Node:
        """Returns new Node object that is a copy of this Node"""
        return Node(self.function, self.parent, self.children)

# endregion


# region TTree Class
class TTree():
    """ Transformation Tree like data structure. Stores Nodes as standard tree.

    Attributes:
        name (str): name of this tree
        root (Node): root node of this tree
        __nodes ([Node], private): reference to each node of this tree

    Args:
        name (str): name of this tree
        root (Node): Node to act as root of this tree
    """

    def __init__(self, name: str, root: Node):
        self.name = name
        self.root = root
        self.root.set_id(0)
        self.id_iterator = 1

        # self.__nodes is just a list containing references of every node in
        # the tree It is just a nice little helper attribute (ez way to
        # check if nodes are contained in the tree)
        self.__nodes = [root]

    def __repr__(self):
        """__repr__ allows us to define the default string representation
        of this class"""
        ret = ""
        for pre, null, node in RenderTree(self.root):
            treestr = u"%s%s" % (pre, node.name)
            ret += treestr.ljust(8) + "\n"
        return ret

    def save(self, file: str):
        """Saves tree as serialized pickle object to specified file path"""
        with open(file, 'wb') as handle:
            pickle.dump(self, handle)

    def set_id(self, node: Node):
        """For use inside of the TTree() class only.
        Sets a node's IDs"""
        node.set_id(self.id_iterator)
        self.id_iterator += 1

    def find_byid(self, id: int):
        """Returns a reference to node with specified id"""
        node_ref = [node for node in PostOrderIter(self.root,
                                                   filter_=lambda n:
                                                   n.id == id)]
        if(len(node_ref) > 0):
            return node_ref[0]
        else:
            raise Exception("Node with id " + id +
                            " does not exist in the TTree")

    def print_tree(self, id=False):
        """Prints a visual representation of the tree with runtime ids for
        each node"""
        for pre, null, node in RenderTree(self.root):
            if(id):
                treestr = u"%s%s (%s)" % (pre, node.name, node.id)
            else:
                treestr = u"%s%s" % (pre, node.name)
            print(treestr.ljust(8))

    def print_nodes_as_list(self):
        """Different from print(). Instead prints each node linearly"""
        print(self.__nodes)

    def add_node(self, target: Node, new_node: Node):
        """Adds a node to the tree as child of target node"""

        # if either arg is not null
        if target and new_node:
            # if target is contained within the tree
            if target in self.__nodes:
                # set parent of new node
                new_node.set_parent(target)

                # update tree to contain new node
                self.__nodes.append(new_node)
                # Set the runtime ID of the new Node
                self.set_id(new_node)
            else:
                raise Exception("New Node cannot be added to target "
                                "because target is not associated "
                                "with this tree.")
        else:
            if not target:
                raise Exception("Target is None")
            elif not new_node:
                raise Exception("Node being added is None")
        pass

    def add_nodes(self, target: Node, nodes: Union[Node, [Node]]):
        """Adds list of Nodes to this tree as children of target Node"""
        if target and nodes:
            if(type(nodes) is not list):  # Allows single node as parameter
                nodes = [nodes]
            # if target is contained within the tree
            if target in self.__nodes:
                for node in nodes:
                    # set parent of new node
                    node.set_parent(target)

                    # update tree to contain new node
                    self.__nodes.append(node)
                    # Set the runtime ID of the new Node
                    if not node.id:
                        self.set_id(node)
            else:
                raise Exception("New Node cannot be added to target "
                                "because target is not associated "
                                "with this tree.")
        else:
            if not target:
                raise Exception("Target is None")
            elif not nodes:
                raise Exception("Nodes being added is None")
        pass

    def add_nodes_byid(self, target_id: int, nodes: Union[Node, [Node]]):
        """Similar to add_nodes(), except finds target by specified id."""
        target = self.find_byid(target_id)
        self.add_nodes(target, nodes)

    def reparent_node(self, parent: Node, node: Node):
        """Reparents node to specified parent"""
        node.set_parent(parent)

    def __add_newpath_byref(self, target: Node, path: [Node]):
        """PRIVATE: Helper function for adding paths by reference to
        target node"""
        if target and len(path) > 0:
            if target in self.__nodes:
                path[0].set_parent(target)
                self.__nodes.append(path[0])
                self.set_id(path[0])
                for i in range(1, len(path)):
                    path[i].set_parent(path[i - 1])
                    self.__nodes.append(path[i])
                    self.set_id(path[i])
            else:
                raise Exception("New Node cannot be added to target "
                                "because target is not associated "
                                "with this tree.")
        else:
            if not target:
                raise Exception("Target is None")
            else:
                raise Exception("No nodes in path")

    def add_newpath(self, target: Node, path: Union[Node, [Node]]):
        """Builds a path starting with target node, and iterating through path,
        inserting these nodes as children of eachother
        (starting with target)"""
        if(type(path) is not list):  # Allows single node as parameter
            path = [path]
        for node in path:
            if node.id:
                # Throw error
                raise Exception("Nodes within new path cannot be "
                                "contained in the tree already.")
        self.__add_newpath_byref(target, path)

    def add_newpath_byid(self, target_id: int, path: Union[Node, [Node]]):
        """Similar to add_newpath, except finds target node by id."""
        if(type(path) is not list):  # Allows single node as parameter
            path = [path]
        # If any node in the new path is already contained in tree, throw error
        for node in path:
            if node.id:
                raise Exception("Nodes within new path cannot be "
                                "contained in the tree already.")
        # Find node with target_id
        target = self.find_byid(target_id)
        self.__add_newpath_byref(target, path)

    def get_pipelines(self) -> [Pipeline]:
        """Generates list of all possible pipelines in the tree."""
        pipelines = []
        leaf_nodes = []

        # grab all leaf nodes to build pipelines from
        for i in range(len(self.__nodes)):
            if not self.__nodes[i].children:
                leaf_nodes.append(self.__nodes[i])

        # construct and append Pipelines from list of leaf_nodes
        for i in range(len(leaf_nodes)):
            new_pipeline = Pipeline(build_node=leaf_nodes[i])
            pipelines.append(new_pipeline)

        return pipelines

    def generate_pipeline(self, build_node: Node) -> Pipeline:
        """Returns a Pipeline built from specified node.
        Recursively traverses tree from build_node to root."""
        if build_node in self.__nodes:
            return Pipeline(build_node=build_node)
        else:
            raise Exception("Node cannot be used to generate pipeline in "
                            "this tree, because Node is not associated "
                            "with this tree.")

    def generate_pipeline_byid(self, id: int) -> Pipeline:
        """Similar to generate_pipeline() except finds node by id."""
        result = None

        for i in range(len(self.__nodes)):
            if self.__nodes[i].id == id:
                result = Pipeline(build_node=self.__nodes[i])
        if result:
            return result
        else:
            raise Exception("ERROR: node of id: " + str(id) +
                            " not found in this tree.")

    def execute_tree(self):
        """Generates and executes every possible pipeline in the tree
        (generates pipelines from leaf nodes, and does not return list)."""
        pipelines = self.get_pipelines()
        for i in range(len(pipelines)):
            pipelines[i].execute()

# endregion


# region Pipeline Class
class Pipeline():
    """ Pipeline object
    Capsulizes each operator along a linear path of operator nodes from TTree()

    Attributes:
        operators ([Callable]): ordered list of callables for this pipeline
                                to execute

    Args:
        <param> "build_node" : Node to build the Pipeline from
        <param> "operators" : list of function pointers to execute linearly

    """

    def __init__(self, build_node: Node = None, operators: [Callable] = None):
        if build_node is not None:
            self.operators = []
            self._generate(build_node)
        else:
            if (operators):
                self.operators = operators if operators is not None else []
            else:
                raise Exception("Build this object by either passing in list"
                                " of Callables, or a compatible \"Node\""
                                " object to build from.")

    def __repr__(self):
        self.print()

    def _generate(self, node: Node):
        """PRIVATE: Used to build the list of callables for this pipeline"""
        self.operators.append(node.function)

        # print("\nTEST: "+ str(self.operators) + "\n")

        while (node.parent is not None):
            self.operators.append(node.parent.function)
            node = node.parent

        self.operators = [op for op in reversed(self.operators)]

    def execute(self, args=None):
        """Executes list of callables linearly, passing return values as
        params of the next callable"""
        result = None

        if args:
            result = self.operators[0](args)
        else:
            result = self.operators[0]()

        for i in range(1, len(self.operators)):
            result = self.operators[i](result)

    def save(self, destination_path: str):
        """Serializes this Pipeline into a .pickle file stored at specified
        file path."""
        with open(destination_path, 'wb') as file:
            pickle.dump(self, file)

    def print(self):
        """DEPRECATED: use print(pipeline).
        Prints pipeline into readable format."""
        if self.operators:
            print("Pipeline:")
            for i in range(len(self.operators)):
                print("\t" + str(i + 1) + ". " + self.operators[i].__name__)

# endregion

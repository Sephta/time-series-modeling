"""
Utility: Tree backend for storing all potential pipelines.
Todo:
Transformation Tree object
    * Some class methods we should add:
        adding a list of nodes as children of target...
        (alec) > TTree.add_nodes (ref to node, [Node] or Node)                    DONE? - NO
        (alec) > TTree.add_nodes_byname (target_name, [Node] or Node)             DONE? - NO
        (alec) > TTree.add_nodes_byid (target_id, [Node] or Node)                 DONE? - NO

        (alec) > TTree.reparent_node() reparents nodes in the tree                DONE? - NO
            (takes children with it)

    * Note: Prof mentioned grabbing pipelines from the leaves of the tree

    * Note: Right now, working concept is that pipelines are just a list of Nodes

    ? Note: Pipeline -> execute_pipeline -> plotting?
    
        (seth) > Pipeline.execute(leaf_node: Node)                                DONE? - YES
        (seth) > TTree.pipelines() -> [Pipeline]                                  DONE? - NO
        (seth) > TTree.execute_tree()                                             DONE? - NO

        (seth) class Pipeline():                                                  DONE? - YES
            def __init__():
                self.nodes = [function pointer thingies]

            def execute()

        (seth) > TTree.generate_pipeline(node: Node) -> Pipeline                  DONE? - NO
        (seth) > TTree.generate_pipeline_byid(id: int) -> Pipeline                DONE? - NO

"""
#region Imports
from __future__ import annotations
from anytree import NodeMixin, RenderTree, render, PostOrderIter
from typing import List, Callable, Union
from tree_utils import copy_path
import pickle
#endregion


#region Module Meta data
__authors__ = "Alec Springel, Seth Tal"
__version__ = "1.0.0"
__emails__ = "aspring6@uoregon.edu, stal@uoregon.edu"
__credits__ = "Kyra Novitzky, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/23/2021"
#endregion


#region Node Class
class Node(NodeMixin):
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
        self.id = id

    def get_id(self):
        return self.id

    def set_parent(self, parent):
        self.parent = parent
        return self.parent
    
    def get_parent(self):
        return self.parent

    def set_children(self, children):
        self.children = children
    
    def get_children(self):
        return self.children

    def copy(self) -> Node:
        return Node(self.function, self.parent, self.children)

#endregion


#region TTree Class
class TTree():
    def __init__(self, name: str, root: Node):
        self.name = name
        self.root = root
        self.root.set_id(0)
        self.id_iterator = 1

        # self.__nodes is just a list containing references of every node in
        # the tree It is just a nice little helper attribute (ez way to
        # check if nodes are contained in the tree)
        self.__nodes = [root]

    def save(self, file: str):
        """Saves tree to as serialized object to specified file path"""
        with open(file, 'wb') as handle:
            pickle.dump(self, handle)

    def set_id(self, node: Node):
        """For use inside of the TTree() class only.
        Sets a node's IDs"""
        node.set_id(self.id_iterator)
        self.id_iterator += 1

    def print_tree(self, id=False):
        """Prints a visual representation of the tree"""
        for pre, null, node in RenderTree(self.root):
            if(id):
                treestr = u"%s%s (%s)" % (pre, node.name, node.id)
            else:
                treestr = u"%s%s" % (pre, node.name)
            print(treestr.ljust(8))

    def print_nodes_as_list(self):
        print(self.__nodes)

    def add_node(self, target: Node, new_node: Node):
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

    def add_nodes(self, target: Node, nodes: [Node]):
        pass

    def add_nodes_byname(self, operator: str, nodes: [Node]):
        pass

    def __add_newpath_byref(self, target: Node, path: [Node]):
        """PRIVATE: Helper function for adding paths by reference to
        target node"""
        if target and len(path) > 0:
            if target in self.__nodes:
                path[0].set_parent(target)
                self.__nodes.append(path[0])
                self.set_id(path[0])
                for i in range(1, len(path)):
                    path[i].set_parent(path[i-1])
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

    # ! We need to come back to this
    # def add_newpath_byname(self, target_name: str, path: Union[Node, [Node]]):
    #     """Builds a path starting with target node, and iterating through path,
    #     inserting these nodes as children of eachother
    #     (starting with target)

    #     Note: User will lose references to original path (need to make copy)
    #     """
    #     if(type(path) is not list):  # Allows single node as parameter
    #         path = [path]
    #     targets = [node for node in PostOrderIter(self.root,
    #                                               filter_=lambda n:
    #                                               n.name == target_name)]
    #     for target in targets:
    #         # Need to make copy of path, otherwise anytree will move the path
    #         # to a new target on each iteration (bc the refs haven't changed)
    #         path_copy = copy_path(path)
    #         self.__add_newpath_byref(target, path_copy)

    def add_newpath_byid(self, target_id: int, path: Union[Node, [Node]]):
        if(type(path) is not list):  # Allows single node as parameter
            path = [path]
        # If any node in the new path is already contained in tree, throw error
        for node in path:
            if node.id:
                raise Exception("Nodes within new path cannot be "
                                "contained in the tree already.")
        targets = [node for node in PostOrderIter(self.root,
                                                  filter_=lambda n:
                                                  n.id == target_id)]

        for target in targets:
            # Need to make copy of path, otherwise anytree will move the path
            # to a new target on each iteration (bc the refs haven't changed)
            self.__add_newpath_byref(target, path)

    def get_pipelines(self) -> [Pipeline]:
        
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
        if build_node in self.__nodes:
            return Pipeline(build_node=build_node)
        else:
            raise Exception("Node cannot be used to generate pipeline in "
                            "this tree, because Node is not associated "
                            "with this tree.")

    def generate_pipeline_byid(self, id: int) -> Pipeline:  
        result = None
        
        for i in range(len(self.__nodes)):
            if self.__nodes[i].id == id:
                result = Pipeline(build_node=self.__nodes[i])
        if result:
            return result
        else:
            raise Exception("Error node of id: " + str(id) + " not found in this tree.")

#endregion


#region Pipeline Class
""" Pipeline object
Capsulizes each operator along a linear path of operator nodes from TTree()

<param> "operators" : list of function pointers to execute linearly

"""
class Pipeline():

    def __init__(self, build_node: Node = None, operators : [Callable] = None):
        if build_node is not None:
            self.operators = []
            self.generate(build_node)
        else:
            if (operators):
                self.operators = operators if operators is not None else []
            else:
                raise Exception("Build this object by either passing in list of Callables," \
                                " or a compatible \"Node\" object to build from.")
    
    def generate(self, node: Node):
        self.operators.append(node.function)
        
        # print("\nTEST: "+ str(self.operators) + "\n")

        while (node.parent is not None):
            self.operators.append(node.parent.function)
            node = node.parent
        
        self.operators = [op for op in reversed(self.operators)]
    
    def execute(self):
        result = self.operators[0]()
        
        for i in range(1, len(self.operators)):
            result = self.operators[i](result)
    
    def save(self, destination_path: str):
        with open(destination_path, 'wb') as file:
            pickle.dump(self, file)

    def print(self):
        if self.operators:
            print("Pipeline:")
            for i in range(len(self.operators)):
                print("\t" + str(i+1) + ". " + self.operators[i].__name__)

#endregion

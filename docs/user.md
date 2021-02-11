# Use and Examples (User Docs)

This file contains the major components of the transformation tree library as well as example uses.

### Authors:

CIS 422 @ University of Oregon  
Team Bitwise  
Ronny Fuentes, Kyra Novitzky, Stephanie Schofield, Alec Springel, Seth Tal

Last modified February 10, 2021

## Setup

To get started, install the library via pip:

```
pip install transformation-tree
```

## Modules & Classes

### Node

```python
from transformation_tree.tree import Node
```

| Method                                | Description                                                         |
| ------------------------------------- | ------------------------------------------------------------------- |
| Node.get_id() -> int                  | Returns the ID of self                                              |
| Node.set_parent(parent: Node) -> Node | Sets self's parent as the passed Node, returns the parent           |
| Node.get_parent() -> Node             | Returns the parent of self                                          |
| Node.set_children(children: [Node])   | Sets self's children equal to children                              |
| Node.get_children() -> [Node]         | Returns self's children                                             |
| Node.copy() -> Node                   | Returns a copy of self with the same function, parent, and children |

### TTree

```python
from transformation_tree.tree import TTree
```

| Method                                                       | Description                                                                         |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| TTree.save(file: str)                                        | Saves the tree                                                                      |
| TTree.find_byid(id: int)                                     | Returns a node in the tree with ID == id                                            |
| TTree.print_tree(id=False: bool)                             | Prints the tree with the option to enable ID's                                      |
| TTree.print_nodes_as_list()                                  | Prints the tree as a list of nodes                                                  |
| TTree.add_node(target: Node, new_node: Node)                 | Adds a single node to the target Node                                               |
| TTree.add_nodes(target: Node, nodes: Node or [Node])         | Adds a single node or list of nodes as children of target                           |
| TTree.add_nodes_byid(target_id: int, nodes: Node or [Node])  | Adds a single node or list of nodes as children of target node with ID == target_id |
| TTree.reparent_node(parent: Node, node: Node)                | Sets the parent of node == parent                                                   |
| TTree.add_newpath(target: Node, path: Node or [Node])        | Adds a path to the target Node                                                      |
| TTree.add_newpath_byid(target_id: int, path: Node or [Node]) | Adds a path to the target node with ID == target_id                                 |
| TTree.get_pipelines() -> [Pipeline]                          | Returns a list of all possible pipelines (derived from leaf nodes)                  |
| TTree.generate_pipeline(build_node: Node) -> Pipeline        | Returns a pipeline that ends with the build_node (built up to the root)             |
| TTree.generate_pipeline_byid(id: int) -> Pipeline            | Returns a pipeline that ends with the Node whose ID == id (built up to the root)    |
| TTree.execute_tree()                                         | Executes the entire transformation tree                                             |

### Pipeline

```python
from transformation_tree.tree import Pipeline
```

| Method                               | Description                                 |
| ------------------------------------ | ------------------------------------------- |
| Pipeline.execute()                   | Executes a pipeline                         |
| Pipeline.save(destination_path: str) | Saves a pipeline to the specified file path |

## How to use the library

### Generating a tree

Before creating a tree a special root method should be created to pass into the root node of the tree:

```python
from transformation_tree.preprocessing import read_from_file

def root():
    return read_from_file("./path/to/csv-data")
```

If you are using the operator functions built into the library the above method is how root should look. Otherwise you should design a root method such that it takes no arguements. If it does take arguements, then when pipelines in the tree execute, arguements will be fed to each function as a tuple.

From here on out it is assumed this library is being used with operator functions built into the library. This means the "data" being fed through the tree will be assumed to be the csv data found in the [time_series_data](https://github.com/Sephta/time-series-modeling/tree/main/time_series_data "Time series data folder") folder.

Each TTree is made up of individual nodes, which are initialized with a function. The TTree can then be initialized with a name and a root node:

```python
from transformation_tree.tree import TTree, Node, Pipeline

# load_data reads a CSV and returns the data as a list of numbers
rootNode = Node(root)  # root refers to the root method defined above
tree = TTree("ExampleTree", rootNode)
```

With the TTree initialized above, we can now define more nodes using operators from the library:

```python
from transformation_tree.preprocessing import denoise, impute_missing_data
from transformation_tree.stats_and_vis import plot_ts

# create two nodes with the preprocessing functions, and one node with visualization
node1 = Node(denoise)
node2 = Node(impute_missing_data)
node3 = Node(plot_ts)
```

To add these nodes to the tree, we have a few options.

#### Adding nodes by reference

We can use references to nodes to add a path or a group of nodes as children.

```python
# ADDING NODES AS CHILDREN:
tree.add_nodes(rootNode, node1)
# OR adds multiple children to rootNode:
tree.add_nodes(rootNode, [node1, node2, node3])

# Adding a path:
path = [node1, node2, node3]
# The nodes will be added as children of one another (last in list will be a leaf node)
tree.add_path(rootNode, path)

```

#### Adding nodes by ID

ID's are automatically assigned to nodes when they are added to the tree. For instance, when a tree is initialized, the rootNode will always be 0. We can then use these ID's to add additional nodes as children.

```python
# This will display ID's
print(tree)

# 0 is the rootNode, adds nodes as children of rootNode
tree.add_nodes_byid(0, [node1, node2, node3])

# Add path by ID
tree.add_path_byid(0, [node1, node2, node3])
```

### Executing and generating pipelines

To execute an entire tree:

```python
tree.execute_tree()
```

Pipelines in this library contain a list of functions that pass their output to the input of the next element. To generate pipelines from our tree:

```python
# Uses the target node as the of the pipeline (builds up to the rootNode)
pipeline = tree.generate_pipeline(node3)

# Using an ID:
pipeline = tree.generate_pipeline_byid(3)

# Returns a list of all pipelines that end at a leaf
list_of_pipelines = tree.get_pipelines()
```

To view or execute a pipeline:

```python
# Print
print(pipeline)

# Execute
pipeline.execute()
```

Finally, if we are happy with a pipeline or transformation tree, we can load and save them like so:

```python
from transformation_tree.tree import load_tree, load_pipeline

tree.save("file/path")
loaded = load_tree("file/path")

pipeline.save("file/path")
loaded_pipe = load_pipeline("file/path")
```

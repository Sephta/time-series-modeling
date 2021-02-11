# Developer Docs

### Authors:

CIS 422 @ University of Oregon  
Team Bitwise  
Ronny Fuentes, Kyra Novitzky, Stephanie Schofield, Alec Springel, Seth Tal

Last modified February 10, 2021

## Setup

Please follow the [setup instructions](https://github.com/Sephta/time-series-modeling/blob/main/docs/install.md) for developers.

## Linter, PEP8 Setup, and contributions

For devleopment, please intall pylint and autopep8. All code should conform with PEP8 guidelines, and should be commented thoroughly.

## A high level overview

This library allows users to contruct transformation trees using Nodes which are initialized with operators (functions). These functions can be defined by the user, or be from one of the included modules, however, these functions must return the parameters for the next operator that comes after them.

The library makes this the user's responsibility, i.e. the library will not ensure compatibility between operators.

## File directories and functionality

### Tree Module

The tree module is responsible for the Node, TTree, and Pipeline class. These classes make up the core functionality of the transformation tree library, with their primary purpose being to contruct trees and pipelines from operators.

There are a few key nuances built into the tree module. It is important to note that Nodes make up trees, but all additions/removals from the tree should be made using the methods defined in the TTree class, not by manually modifying the parents and children of individual nodes. Furthermore, Nodes are assigned ID's when they are added to the tree. These ID's are unique, and have no correlation to the number of nodes in the tree. ID's are assigned by continually incrementing a counter within a tree object, making note of the next available ID.

These ID's provide a valuable tool for data scientists, as they can work through jupyter notebooks (and other visual tools) without references to the original nodes.

### Preprocessing Module

The preprocessing module contains operators for use within the tree module. These functions modify the data in its early stages to make it usable or fit a particular shape.

### Forecasting Module

The forecasting module also contains operators responsible for
machine learning techniques, allowing the user to make predictions about the data and create ML pipelines.

### Stats and Visualization Module

The stats and visualization module contain all the functions needed for graphing and visualizing the data.

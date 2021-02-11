# Transformation Tree Library

This transformation tree library allows you to quickly build out possible modification paths for input data, and test various outcomes. The library also allows these pipelines and trees to be saved and loaded with ease. The library provides four major modules to build out transformation trees and pipelines, as well as provided operators and visualization tools to help build a pipeline.

Links: [User Documentation](https://github.com/Sephta/time-series-modeling/blob/main/docs/user.md), [Developer Documentation](https://github.com/Sephta/time-series-modeling/blob/main/docs/dev.md), [Install Instructions](https://github.com/Sephta/time-series-modeling/blob/main/docs/install.md), [PyPi package info](https://pypi.org/project/transformation-tree/ "PyPi package info")

### Authors:

CIS 422 @ University of Oregon  
Team Bitwise  
Ronny Fuentes, Kyra Novitzky, Stephanie Schofield, Alec Springel, Seth Tal

Last modified February 10, 2021

## Installation

### For Users:

```
pip install transformation-tree
```

See the documentation below for use cases and examples.

### For Developers:

- make sure python is installed and added to PATH
- check python version (>=3.7.9)
- make sure pip is installed
- clone the repository:

```
git clone https://github.com/Sephta/time-series-modeling.git
```

- install dependencies:

```
pip install -r requirements.txt
```

All source code can be found within transformation_tree.

## Using the library

There are four major modules in the library:

- tree
- preprocessing
- forecasting
- stats_and_vis

which can be imported like so:

```
from transformation_tree.tree import *
from transformation_tree.preprocessing import *
from transformation_tree.forecasting import *
from transformation_tree.stats_and_vis import *
```

To learn how to create a transformation tree, please visit the [User Documentation](https://github.com/Sephta/time-series-modeling/blob/main/docs/user.md).

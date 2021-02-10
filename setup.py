import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="transformation-tree",
    version="1.1.0",
    python_requires=">=3.7.9",
    description="Transformation Tree library developed for CIS 422 @ \
                 University of Oregon",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Sephta/time-series-modeling",
    author="Seth Tal, Alec Springel, Ronny Fuentes, Stephanie Schofield, Kyra \
            Novitzky",
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
    install_requires=["scikit-learn",
                      "anytree",
                      "pickle-mixin",
                      "pandas",
                      "numpy",
                      "scipy",
                      "statsmodels",
                      "seaborn",
                      "matplotlib"
                      ],
)

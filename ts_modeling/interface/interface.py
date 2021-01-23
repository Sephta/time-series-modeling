#!/usr/bin/env/python

"""
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis
Utility: Command line interface for building pipelines.
"""

# import statements below
import sys

__authors__ = "Alec Springel"
__version__ = "1.0.0"
__emails__ = "aspring6@uoregon.edu"
__credits__ = "Kyra Novitzky, Seth Tal, Ronny Fuentes, Stephanie Schofield"
__date__ = "01/22/2021"


class Interface:
    def main_menu(self):
        """Method for generating main menu prompt--the entry point
        for the CLI"""
        for line in sys.stdin:
            # Remove trailing character
            line = line.rstrip()
            if 'exit' == line:
                break
            print(f'Input : {line}')
            return "Not implemented yet"

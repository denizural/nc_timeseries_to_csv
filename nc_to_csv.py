#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""nc_to_csv.py:
A sample command-line tool to convert 2D NetCDF data to CSV time series
"""

__author__ = "Deniz Ural"
__authors__ = ["Deniz Ural"]
__maintainer__ = "Deniz Ural"
__contact__ = "denizural86@gmail.com"
__email__ = "denizural86@gmail.com"
__copyright__ = ""
__license__ = "GPLv3"
__date__ = "2023/02/06"
__status__ = "Development"  # Production
__version__ = "0.0.1"

import argparse
import sys
import pathlib

import netCDF4 as nc4
import pandas as pd

prog_name = pathlib.Path(sys.argv[0]).name

parser = argparse.ArgumentParser(
    prog=prog_name,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

# get the input NetCDF file
parser.add_argument(
    "-f",
    "--file",
    type=str,
    required=True,
    help="input NetCDF file",
    default=None,
)

# parse command line arguments
cmd_args = parser.parse_args()

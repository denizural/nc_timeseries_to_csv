#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""nc_to_csv.py:
A sample command-line tool to convert 1D NetCDF data to CSV time series
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

# Open the netCDF file
nc_file = nc4.Dataset(cmd_args.file, "r")

# get the coordinates
lat = nc_file.variables["latitude"][:]
lon = nc_file.variables["longitude"][:]

# get the wind data at the fixed location
u100 = nc_file.variables["u100"][:,0,0]
v100 = nc_file.variables["v100"][:,0,0]

# get dates
dates = nc_file.variables["time"]
dates = nc4.num2date(dates, dates.units, dates.calendar)

nc_file.close()

# Create a DataFrame with the extracted information
data = {'date': dates, 'u100': u100, 'v100': v100}
df = pd.DataFrame(data)



"""
-------------------------------------------------------------------------------
|  _                                                                          |
| | |_ _ __(_) | _(_) |_                                                      |
| | __| '__| | |/ / | __|                                                     |
| | |_| |  | |   <| | |_                                                      |
|  \__|_|  |_|_|\_\_|\__|                                                     |
|                                                                             |
| A Pythonic Approach to Actuarial Reserving                                  |
| Copyright 2018 James D. Triveri                                             |
-------------------------------------------------------------------------------
"""
import os
import os.path
import sys
import collections
import datetime
import pathlib
import os.path
import warnings
import numpy as np
import pandas as pd
import scipy
from .datasets import dataref
from .triangle import totri
from .utils import (
    _load, _get_datasets, _get_lrdb_lobs, _get_lrdb_groups, _get_lrdb_specs,
    )

# Initialize dataset loading utility and lrdb-related functions.
lrdb_path = dataref["lrdb"]
load = _load(dataref=dataref)
get_datasets = _get_datasets(dataref=dataref)
get_lrdb_lobs = _get_lrdb_lobs(lrdb_path=lrdb_path)
get_lrdb_groups = _get_lrdb_groups(lrdb_path=lrdb_path)
get_lrdb_specs = _get_lrdb_specs(lrdb_path=lrdb_path)

__version__ = "0.2.10"

# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['HelloSayer']

# Cell
import math
from dataclasses import dataclass, field
from pathlib import PosixPath
from typing import List

import planets
from heat1d.plotting import plot_last_surface_cooling
from scipy.spatial.distance import pdist, squareform

import heat1d


# Cell
class HelloSayer:
    """Say hello to `to` using `say_hello`

    Parameters
    ----------
    to: String to whom say hello
    """

    def __init__(self, to):
        self.to = to

    def say(self):
        "Do the saying"
        return say_hello(self.to)
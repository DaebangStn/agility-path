from random import randint
from enum import Enum, auto
from abc import ABC, abstractmethod
from math import sin, cos, sqrt, atan2, radians
from typing import List, Tuple, Dict, Union, Any

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib import transforms


GRID_SIZE = 0.5


def round_gs(x: Any) -> Any:
    if isinstance(x, float):
        return round(x / GRID_SIZE) * GRID_SIZE
    elif isinstance(x, list):
        return [round_gs(i) for i in x]
    elif isinstance(x, tuple):
        return tuple(round_gs(i) for i in x)
    else:
        raise TypeError("Unsupported type. The input must be a float, list, or tuple of floats.")


def add_coord(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> Tuple[float, float]:
    return coord1[0] + coord2[0], coord1[1] + coord2[1]

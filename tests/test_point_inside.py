import pytest
import numpy as np

from math import pi

import geom.data as dat
from geom.ops import point_inside


def test_point_inside_circle():
    circ = dat.Circle((1, 1), r=(1))
    assert point_inside(circ, [1, 1]) == True
    assert point_inside(circ, [0, 0]) == False
    assert point_inside(circ, [1, 0]) == True

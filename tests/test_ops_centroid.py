import pytest
import numpy as np
from numpy.testing import assert_array_equal

import geom.data as dat
from geom.ops import centroid


def test_centroid_circle():
    circ = dat.Circle([1, 2], r=3)
    assert_array_equal(centroid(circ), [1, 2])


def test_centroid_rect():
    rect = dat.Rectangle([1, 2], [2, 3])
    assert_array_equal(centroid(rect), [1, 2])


def test_centroid_poly():
    poly = dat.Polygon([[4, 5], [20, 25], [30, 6]])
    assert_array_equal(centroid(poly), [18, 12])


def test_centroid_grid():
    grid = dat.Grid((0.1, 0.1), (0.8, 0.8))
    assert_array_equal(centroid(grid), [0.5, 0.5])

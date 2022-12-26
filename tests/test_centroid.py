import pytest
import numpy as np
from numpy.testing import assert_array_equal

import geom.data as dat
from geom.ops import centroid


def test_centroid_circle():
    circ = dat.Circle([1, 2], r=3)
    assert_array_equal(centroid(circ), [1, 2])


def test_centroid_rect():
    rect = dat.Rect([1, 2], [2, 3])
    assert_array_equal(centroid(rect), [2, 3.5])


def test_centroid_poly():
    poly = dat.Polygon([[4, 5], [20, 25], [30, 6]])
    assert_array_equal(centroid(poly).coords[0], [18, 12])

import pytest
import numpy as np

import geom.data as dat

from geom.ops import bounds


def test_bounds_arc():
    pass
    # circ = dat.Circle((1, 1), r=1)
    # res = bounds(circ)
    # assert res == [0, 0, 0, 0]


def test_bounds_circle():
    circ = dat.Circle((1, 1), r=1)
    res = bounds(circ)
    np.testing.assert_array_equal(res, [0, 0, 2, 2])


# def test_bounds_cubic():
#     circ = dat.Circle((1, 1), r=1)
#     res = bounds(circ)
#     assert res == [0, 0, 0, 0]

# def test_bounds_ellipse():
#     circ = dat.Circle((1, 1), r=1)
#     res = bounds(circ)
#     assert res == [0, 0, 0, 0]


def test_bounds_grid():
    grid = dat.Grid([1, 2], [3, 4], [12, 13])
    res = bounds(grid)
    np.testing.assert_array_equal(res, [1, 2, 3, 4])


def test_bounds_line():
    line = dat.Line([1, 2], [0, 0])
    res = bounds(line)
    np.testing.assert_array_equal(res, [0, 0, 1, 2])


# def test_bounds_point():
#     pts = dat.Point([[0, 0], [2, 1], [0.5, 0.75], [1, 2]])
#     res = bounds(pts)
#     np.testing.assert_array_equal(res, [0, 0, 2, 2])


def test_bounds_poly():
    poly = dat.Polygon([[0, 0], [2, 1], [1, 2]])
    res = bounds(poly)
    np.testing.assert_array_equal(res, [0, 0, 2, 2])


def test_bounds_rect():
    rect = dat.Rect((1, 2), (3, 4))
    res = bounds(rect)
    np.testing.assert_array_equal(res, [1, 2, 3, 4])


def test_bounds_triangle():
    tri = dat.Triangle([[0, 0], [1, 0], [1, 1]])
    res = bounds(tri)
    np.testing.assert_array_equal(res, [0, 0, 1, 1])

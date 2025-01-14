import pytest
import numpy as np
from numpy.testing import assert_array_equal, assert_almost_equal

import geom.data as dat
from geom.ops import distance


def test_distance_point_to_line():
    # Horizontal line from (0,0) to (4,0)
    line = dat.Line([0, 0], [4, 0])

    # Point directly above middle of line
    assert_almost_equal(distance(line, [2, 3]), 3.0)

    # Point at start of line
    assert_almost_equal(distance(line, [0, 0]), 0.0)

    # Point at end of line
    assert_almost_equal(distance(line, [4, 0]), 0.0)

    # Point beyond start of line
    assert_almost_equal(distance(line, [-1, 0]), 1.0)

    # Point beyond end of line
    assert_almost_equal(distance(line, [5, 0]), 1.0)


def test_distance_point_to_angled_line():
    # 45 degree line from (0,0) to (1,1)
    line = dat.Line([0, 0], [1, 1])

    # Point on the line
    assert_almost_equal(distance(line, [0.5, 0.5]), 0.0)

    # Point perpendicular to middle of line
    assert_almost_equal(distance(line, [0, 1]), 0.7071067811865476)  # 1/√2


def test_distance_point_to_vertical_line():
    # Vertical line from (0,0) to (0,3)
    line = dat.Line([0, 0], [0, 3])

    # Point to right of line
    assert_almost_equal(distance(line, [2, 1.5]), 2.0)

    # Point on line
    assert_almost_equal(distance(line, [0, 1.5]), 0.0)


def test_distance_point_to_zero_length_line():
    # Line with same start and end point
    line = dat.Line([1, 1], [1, 1])

    # Should measure distance to the point
    assert_almost_equal(distance(line, [4, 5]), 5.0)  # Distance from (1,1) to (4,5)

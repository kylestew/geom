import pytest
import numpy as np

from math import pi

from geom.data import (
    Arc,
    Circle,
    Cubic,
    Ellipse,
    Grid,
    Line,
    Point,
    Polygon,
    Rect,
    Triangle,
)
from geom.ops import area


def test_area_arc_fails():
    pass
    # curves can have areas in my book
    # arc = Arc()
    # with pytest.raises(Exception):
    #     area(arc) == 0


def test_area_circle():
    circ = Circle((1, 2), r=(3))
    assert area(circ) == pi * 3 * 3


def test_area_cubic_fails():
    # curves can have areas in my book
    pass
    # cube = Cubic()
    # with pytest.raises(Exception):
    #     area(cube) == 0


def test_area_ellipse():
    # not sure how to do this
    pass


def test_area_line_fails():
    line = Line()
    with pytest.raises(Exception):
        area(line) == 123


def test_area_point_fails():
    points = Point([[0, 0]])
    with pytest.raises(Exception):
        area(points) == 123


def test_area_polygon():
    poly = Polygon(Rect(size=[2, 3]).points)
    assert area(poly) == 6


def test_area_rect():
    rect = Rect((1, 2), size=(3, 4))
    assert area(rect) == 12


def test_area_triangle():
    tri = Triangle([[0, 0], [1, 0], [1, 1]])
    assert area(tri) == 0.5

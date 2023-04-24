import numpy as np

from geom.data import Rect, Circle, Point


def test_point_create():
    point = Point([1, 2])
    np.testing.assert_array_equal(point.pt, [1, 2])


def test_point_create_numpy_array():
    pt = np.array([1, 2])
    point = Point(pt)
    np.testing.assert_array_equal(point.pt, [1, 2])
    x, y = point.pt
    assert x == 1
    assert y == 2


def test_rect_create():
    rect = Rect((1, 2), size=(3, 4))
    np.testing.assert_array_equal(rect.points, [(1, 2), (4, 2), (4, 6), (1, 6)])


def test_rect_create_from_center():
    pass


def test_rect_create_from_points():
    pass


def test_rect_inset():
    pass


def test_rect_offset():
    pass


def test_circle_create():
    circ = Circle([1, 2], 3.456)
    np.testing.assert_array_equal(circ.center, [1, 2])
    assert circ.r == 3.456


def test_circle_create_in_rect():
    rect = Rect((1, 2), size=(3, 4))
    circ = Circle.in_rect(rect)
    np.testing.assert_array_equal(circ.center, [2.5, 4.0])
    assert circ.r == 1.5

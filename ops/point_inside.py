from geom.data.rect import Rect
from geom.data.circle import Circle
from geom.data.points import Points
from geom.data.polygon import Polygon
from .vertices import vertices

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from numpy import array


def _point_inside(poly_pts, pt):
    """
    poly_pts - points defining the polygon
    pt - point to check
    returns: True/False
    """
    [x, y] = pt
    point = Point(x, y)
    polygon = Polygon(poly_pts)
    return polygon.contains(point)


def point_inside(dat, pt):
    """
    Determines if a given point is within the shape
    For `Points`, determines if in set of points (exact point exists in array)
    """
    if isinstance(dat, Rect):
        return _point_inside(vertices(dat), pt)

    elif isinstance(dat, Circle):
        # skip sqrt for speed
        # dist squared <= radius squared
        x1, y1 = dat.origin
        x2, y2 = pt
        return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) <= dat.r * dat.r

    elif isinstance(dat, Points):
        return (dat.points == array(pt)).all(1).any()

    elif isinstance(dat, Polygon):
        return _point_inside(dat.points, pt)

    else:  # Line
        # TODO: can implement a "point in segment" on a line algo
        return False

from geom.data.rect import Rect
from geom.data.circle import Circle
from geom.data.polygon import Polygon

from geom.ops.vertices import vertices

from shapely.geometry import Point as SPoint
from shapely.geometry.polygon import Polygon as SPoly

from numpy import array


def _point_inside(poly_pts, pt):
    """
    poly_pts - points defining the polygon
    pt - point to check
    returns: True/False
    """
    [x, y] = pt
    point = SPoint(x, y)
    polygon = SPoly(poly_pts)
    return polygon.contains(point)


def point_inside(dat, pt):
    """
    Determines if a given point is within the shape
    """
    if isinstance(dat, Rect) or isinstance(dat, Polygon):
        return _point_inside(vertices(dat), pt)

    elif isinstance(dat, Circle):
        # skip sqrt for speed
        # dist squared <= radius squared
        x1, y1 = dat.center
        x2, y2 = pt
        return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) <= dat.r * dat.r

    else:  # Line
        # TODO: can implement a "point in segment" on a line algo
        return False

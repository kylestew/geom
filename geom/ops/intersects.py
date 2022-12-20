from geom.data.line import Line
from geom.data.circle import Circle

from geom.ops.vertices import vertices

from shapely.geometry import LineString
from shapely.geometry import Polygon


def intersects(dat, other):
    """
    Checks if given object intersects with another object
    (can only do two lines right now)
    """
    if isinstance(dat, Circle) and isinstance(other, Circle):
        # simple circle-circle intersection
        from math import dist

        p1 = dat.origin
        r1 = dat.r
        p2 = other.origin
        r2 = other.r
        return dist(p1, p2) < (r1 + r2)

    if isinstance(dat, Line):
        a = LineString(dat.points)
    elif isinstance(dat, Circle) or isinstance(dat, Rect):
        a = Polygon(vertices(dat))
    else:
        raise Exception("NOT IMPLEMENTED")

    if isinstance(other, Line):
        b = LineString(other.points)
    elif isinstance(other, Circle) or isinstance(other, Rect):
        b = Polygon(vertices(other))
    else:
        raise Exception("NOT IMPLEMENTED")

    return a.intersects(b)

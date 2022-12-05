from geom.data.line import Line
from geom.data.circle import Circle

from shapely.geometry import LineString


def intersects(dat, other):
    """
    Checks if given object intersects with another object
    (can only do two lines right now)
    """

    if isinstance(dat, Line):
        a = LineString(dat.points)
        if isinstance(other, Line):
            b = LineString(other.points)
            return a.intersects(b)

    if isinstance(dat, Circle) and isinstance(other, Circle):
        from math import dist

        p1 = dat.origin
        r1 = dat.r
        p2 = other.origin
        r2 = other.r

        return dist(p1, p2) < (r1 + r2)

    return False

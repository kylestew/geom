from geom.data.line import Line

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

    return False

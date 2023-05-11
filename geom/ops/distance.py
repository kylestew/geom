from math import sqrt

from geom.ops.centroid import centroid

from geom.data.point import Point

def distance(dat, pt):
    """
    Determines the distance between a given 'pt' and geom data object

    - dat: data.Geom object
    - pt: naked point array or Point object
    """
    x1, y1 = centroid(dat)

    if isinstance(dat, Point):
        x2, y2 = pt.pt
    else:
        x2, y2 = pt

    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
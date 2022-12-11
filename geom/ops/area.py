from geom.data.rect import Rect
from geom.data.circle import Circle
from geom.data.polygon import Polygon
from math import pi

from shapely.geometry import Polygon as SPoly


def area(dat):
    """
    Computes the possibly signed (unsigned by default) surface area of given `shape`.

    For curves, lines, point clouds and rays the function returns 0.
    """
    if isinstance(dat, Rect):
        return dat.w * dat.h

    elif isinstance(dat, Circle):
        return pi * dat.r * dat.r

    # elif isinstance(dat, Polygon):
    #     raise Exception("NOT IMPLEMENTED")

    else:
        return SPoly(dat.points).area

from math import pi

from geom.data import (
    Arc,
    Circle,
    Cubic,
    Ellipse,
    Grid,
    Line,
    Points,
    Polygon,
    Rect,
    Triangle,
)

from geom.ops.vertices import vertices

from shapely.geometry import Polygon as SPoly

from ._lib.guards import throws_impossible_for


def area(dat):
    """
    Computes the possibly signed (unsigned by default) surface area of given `shape`.

    For curves, lines, point clouds and rays the function returns 0.
    """
    throws_impossible_for(dat, [Line, Points])

    if isinstance(dat, Circle):
        return pi * dat.r * dat.r

    elif isinstance(dat, Rect):
        return dat.w * dat.h

    else:
        print(vertices(dat))
        return SPoly(vertices(dat)).area

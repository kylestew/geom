from geom.data.line import Line
from geom.data.circle import Circle
from geom.data.sphere import Sphere

from geom.ops.vertices import vertices

from shapely.geometry import LineString
from shapely.geometry import Polygon

from math import dist


def intersects(dat, other):
    if (isinstance(dat, Circle) and isinstance(other, Circle)) or (
        isinstance(dat, Sphere) and isinstance(other, Sphere)
    ):
        # simple circle-circle or sphere-sphere intersection
        p1 = dat.center
        r1 = dat.r
        p2 = other.center
        r2 = other.r
        return dist(p1, p2) < (r1 + r2)

    if isinstance(dat, Line):
        a = LineString(dat.points)
    else:
        a = Polygon(vertices(dat))

    if isinstance(other, Line):
        b = LineString(other.points)
    else:
        b = Polygon(vertices(other))

    return a.intersects(b)

from geom.data.rect import Rect
from geom.data.circle import Circle
from numpy import array, linspace, column_stack, cos, sin
from math import pi

DEFAULT_SAMPLES = 32


def vertices(dat, n=DEFAULT_SAMPLES):
    if isinstance(dat, Rect):
        p = (dat.x, dat.y)
        q = (p[0] + dat.w, p[1] + dat.h)
        return array([p, (q[0], p[1]), q, (p[0], q[1])])

    elif isinstance(dat, Circle):
        a = linspace(0, pi * 2, n + 1) + dat.theta
        circ = dat.origin + column_stack((cos(a), sin(a))) * dat.r
        return circ[:-1]

    elif hasattr(dat, "points") == True:
        return dat.points

    else:
        # hope its an iterable full of vertices
        return dat

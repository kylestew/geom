from geom.data.rect import Rect
from geom.data.points import Points

from geom.ops.bounds import bounds
from geom.ops.area import area
from geom.ops.point_inside import point_inside

from geom.ops.internal.poison import PoissonDisc

from random import uniform
import math


def random_point_in(bounds):
    xmin, ymin, xmax, ymax = bounds
    while True:
        x = uniform(xmin, xmax)
        y = uniform(ymin, ymax)
        yield [x, y]


def scatter_pts(dat, density=0.9):
    """
    Scatters points in bounds of shape.
    Shape must have a usable point_inside, and bounds implementation

    returns: 0 or more points scattered into the area of the polygon
    note: returns no points if the shape bounds cannot be determined
    """

    r = math.sqrt(area(dat)) * (1.0 - density)

    if isinstance(dat, Rect):
        disc = PoissonDisc(width=dat.w, height=dat.h, r=r)
        pts = disc.sample()
        pts = [(x + dat.x, y + dat.y) for (x, y) in pts]
        return Points(pts)

    b = bounds(dat)
    if b == None:
        return []

    # TODO: use poison for all
    rgen = random_point_in(b)
    out = []
    for _ in range(num):
        while True:
            pt = next(rgen)
            if point_inside(dat, pt):
                out.append(pt)
                break

    return out

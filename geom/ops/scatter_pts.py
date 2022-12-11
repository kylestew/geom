#%%
from geom.data.rect import Rect
from geom.data.points import Points

from geom.ops.bounds import bounds
from geom.ops.area import area
from geom.ops.point_inside import point_inside

from geom.internal.poison import PoissonDisc

# from random import uniform
import math


"""
def random_point_in(bounds):
    xmin, ymin, xmax, ymax = bounds
    while True:
        x = uniform(xmin, xmax)
        y = uniform(ymin, ymax)
        yield [x, y]
"""


def scatter_pts(dat, density=0.9):
    """
    Uses Poisson sampling!

    Scatters points in the bounds of a given shape.
    (Shape must have a usable bounds implementation)

    returns: 0 or more points scattered into the area of the bounds
    note: returns no points if the shape bounds cannot be determined
    """

    # found a rectangular boundary covering poly area
    b = bounds(dat)
    if b == None:
        return []
    x, y, w, h = b

    # determine density setting for poisson sampling
    r = math.sqrt(area(dat)) * (1.0 - density)

    # sample points in rect boundary
    disc = PoissonDisc(width=w, height=h, r=r)
    pts = disc.sample()
    pts = [(px + x, py + y) for (px, py) in pts]

    pts = list(filter(lambda pt: point_inside(dat, pt) == True, pts))

    return Points(pts)

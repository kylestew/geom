from geom.ops.bounds import bounds
from geom.ops.area import area
from geom.ops.point_inside import point_inside

from geom.internal.poison import PoissonDisc

from random import uniform
import math


def random_point_in(bounds):
    xmin, ymin, xmax, ymax = bounds
    while True:
        x = uniform(xmin, xmax)
        y = uniform(ymin, ymax)
        yield [x, y]


def scatter_pts(dat, density=0.8, poisson=False):
    """
    Uses Poisson sampling!

    Scatters points in the bounds of a given shape.
    (Shape must have a usable bounds and point_inside implementation)

    - density: density of sampling (behaves weird when using Poisson)
    - poisson: whether or not to use Poisson sampling

    returns: 0 or more points scattered into the area of the bounds
    note: returns no points if the shape bounds cannot be determined
    """

    if poisson:
        return _poisson_sample_pts(dat, density)

    b = bounds(dat)
    if b == None:
        return []

    # arbitrary "dense" number, idk!
    # grows exponentially with area - careful!
    num = int(area(dat) * math.sqrt(density) * 1000)

    rgen = random_point_in(b)
    out = []
    for _ in range(num):
        while True:
            pt = next(rgen)
            if point_inside(dat, pt):
                out.append(pt)
                break

    return out


def _poisson_sample_pts(dat, density=0.9):
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

    return list(filter(lambda pt: point_inside(dat, pt) == True, pts))



"""
from geom.ops import centroid, bounds, point_inside
from random import gauss
from numpy import append
from numpy.random import uniform


def gaussian_point_in(dat, sigma=0.5):
    """
    selects a random point from a guassian distribution shaped by given bounds

    - dat: bounds geom.data (must implement bounds, centroid, and point_inside)
    - sigma [0.5]: guassian distro spread value

    returns: point gauranteed to be inside bounds
    """
    cx, cy = centroid(dat)
    _, _, w, h = bounds(dat)

    def throw():
        x = gauss(cx, sigma * w)
        y = gauss(cy, sigma * h)
        return x, y

    pt = throw()
    while point_inside(dat, pt) == False:
        pt = throw()
    return pt


def uniform_point_in(dat):
    """
    selects a unifrom random point inside the given bounds

    - dat: bounds geom.data (must implement bounds, centroid, and point_inside)

    returns: point gauranteed to be inside bounds
    """
    x, y, w, h = bounds(dat)
    x = uniform(x, x + w, 1)
    y = uniform(y, y + h, 1)
    return tuple(append(x, y))

"""
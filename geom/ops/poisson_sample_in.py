import math

from geom.ops.bounds import bounds
from geom.ops.area import area
from geom.ops.point_inside import point_inside

from geom.internal.poison import PoissonDisc


def poisson_sample_in(dat, density=0.9):
    """
    Scatters points in the bounds of a given shape using Poisson sampling

    (`dat` must implement: `bounds`, `point_inside`)

    - density: density of sampling (behaves weird when using Poisson)
    - poisson: whether or not to use Poisson sampling

    returns: 0 or more points scattered into the area of the bounds
    note: returns no points if the shape bounds cannot be determined
    """

    # found a rectangular boundary covering poly area
    b = bounds(dat)
    if b == None:
        return []
    x, y, w, h = b

    # determine density setting for poisson sampling
    density = min(density, 0.99)
    r = math.sqrt(area(dat)) * (1.0 - density)

    # sample points in rect boundary
    disc = PoissonDisc(width=w, height=h, r=r)
    pts = disc.sample()
    pts = [(px + x, py + y) for (px, py) in pts]

    return list(filter(lambda pt: point_inside(dat, pt) == True, pts))

from geom.ops.bounds import bounds
from geom.ops.point_inside import point_inside

from geom.internal.poison import PoissonDisc


def poisson_sample_in(dat, r=0.1):
    """
    ** CAREFUL: this can take a lot of time to return if r is small **
    Scatters points in the bounds of a given shape using Poisson sampling

    (`dat` must implement: `bounds`, `point_inside`)

    - r: radius around each point (determines density)

    returns: 0 or more points scattered into the area of the bounds
    note: returns no points if the shape bounds cannot be determined
    """
    # found a rectangular boundary covering poly area
    b = bounds(dat)
    if b == None:
        return []
    x, y, w, h = b

    # sample points in rect boundary
    disc = PoissonDisc(width=w, height=h, r=r)
    pts = disc.sample()
    pts = [(px + x, py + y) for (px, py) in pts]

    return list(filter(lambda pt: point_inside(dat, pt) == True, pts))

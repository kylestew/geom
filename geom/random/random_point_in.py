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

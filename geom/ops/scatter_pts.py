from enum import Enum

import random

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

from geom.ops.bounds import bounds
from geom.ops.centroid import centroid
from geom.ops.point_inside import point_inside

from ._lib.guards import throws_impossible_for


class RandomSampling(Enum):
    RANDOM = 0
    UNIFORM = 1
    GAUSSIAN = 2


# def gaussian_point_in(dat, sigma=0.5):
def scatter_pts(
    dat, num=12, seed=None, sampling=RandomSampling.RANDOM, sigma=0.5
):
    """
    Scatters points in the bounds of a given GEO.DAT shape.

    (`dat` must implement: `bounds`, `point_inside`)

    - num: number of random point to return
    - seed: random seed to use
    - sampling: type of randomness to use [Random, Uniform, Guassian]
    - sigma: (for gaussian sampling) spread of gaussian function

    returns: `num` points scattered into the bounds of the `dat` geo
    note: returns no points if the shape bounds cannot be determined
    """
    throws_impossible_for(dat, [Arc, Cubic, Grid, Line, Points])

    bnds = bounds(dat)
    if bnds == None:
        raise Exception("Does not implement `bounds`")

    if seed == None:
        seed = random.random() * 1230129
    random.seed(seed)

    # random function that finds a point withing the rough bounds of the shape
    if sampling == RandomSampling.UNIFORM:
        rgen = _uniform_point_in(dat)
    elif sampling == RandomSampling.GAUSSIAN:
        rgen = _gauss_point_in(dat, sigma)
    else:
        rgen = _random_point_in(dat)

    # invoke random FN, throwing away points outside exact shape boundaries
    out = []
    for _ in range(num):
        while True:
            pt = next(rgen)
            if point_inside(dat, pt):
                out.append(pt)
                break

    return out


def _random_point_in(dat):
    x, y, w, h = bounds(dat)
    while True:
        # [0, 1]
        rx = random.random() * w + x
        ry = random.random() * h + y
        yield [rx, ry]


def _uniform_point_in(dat):
    x, y, w, h = bounds(dat)
    while True:
        rx = random.uniform(x, x + w)
        ry = random.uniform(y, y + h)
        yield [rx, ry]


def _gauss_point_in(dat, sigma):
    # NOTE: does not gaurantee inside bounds
    cx, cy = centroid(dat)
    _, _, w, h = bounds(dat)

    def throw():
        rx = random.gauss(cx, sigma * w)
        ry = random.gauss(cy, sigma * h)
        return [rx, ry]

    while True:
        pt = throw()
        yield pt

from numpy import array
import math

from geom.data.rect import Rect
from geom.data.circle import Circle
from geom.data.points import Points
from geom.data.line import Line
from geom.data.grid import Grid
from geom.data.polygon import Polygon


def bounds(dat):
    """
    Returns a tight rect that contains all geometry

    rect: (x, y, w, h)
    """
    if isinstance(dat, Rect):
        return (dat.x, dat.y, dat.w, dat.h)

    if isinstance(dat, Grid):
        return (dat._x, dat._y, dat._w, dat._h)

    elif isinstance(dat, Circle):
        r = dat.r
        return bounds(Rect(dat.center - array((r, r)), (2 * dat.r, 2 * dat.r)))

    else:
        pts = dat.points
        min_x = math.inf
        min_y = math.inf
        max_x = -math.inf
        max_y = -math.inf
        for pt in pts:
            x, y = pt
            min_x = min(x, min_x)
            min_y = min(y, min_y)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
        return [min_x, min_y, max_x - min_x, max_y - min_y]

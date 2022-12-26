from numpy import array
import math

from geom.data.rect import Rect
from geom.data.circle import Circle
from geom.data.points import Points
from geom.data.line import Line

from geom.ops.vertices import vertices

from shapely.geometry import Polygon


def bounds(dat):
    """
    Returns a tight rect that contains all geometry

    rect: (x, y, w, h)
    """
    if isinstance(dat, Rect):
        return (dat.x, dat.y, dat.w, dat.h)

    elif isinstance(dat, Circle):
        r = dat.r
        return bounds(Rect(dat.center - array((r, r)), (2 * dat.r, 2 * dat.r)))

    elif isinstance(dat, Points) or isinstance(dat, Line):
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

    else:
        print(vertices(dat))
        return Polygon(vertices(dat)).bounds

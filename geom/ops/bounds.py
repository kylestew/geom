from geom.data.rect import Rect
from geom.data.circle import Circle
from shapely.geometry import Polygon


def bounds(dat):
    if isinstance(dat, Rect):
        return (dat.x, dat.y, dat.x + dat.w, dat.y + dat.h)

    elif isinstance(dat, Circle):
        x, y = dat.origin
        return bounds(Rect(x, y, 2 * dat.r, 2 * dat.r))

    else:
        return Polygon(dat.points).bounds

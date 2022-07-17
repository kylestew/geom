from geom.data.rect import Rect
from geom.data.circle import Circle
from geom.data.line import Line
from numpy import array, sum
from geom.ops.point_at import point_at
from geom.ops.vertices import vertices


def centroid(dat):
    """
    Computes centroid of given shape
    """
    if isinstance(dat, Rect):
        return dat.x + dat.w / 2.0, dat.y + dat.h / 2.0

    elif isinstance(dat, Circle):
        return dat.origin

    elif isinstance(dat, Line):
        return point_at(dat, 0.5)

    else:
        """
        https://stackoverflow.com/questions/23020659/fastest-way-to-calculate-the-centroid-of-a-set-of-coordinate-tuples-in-python-wi
        """
        pts = vertices(dat)
        length = pts.shape[0]
        sum_x = sum(pts[:, 0])
        sum_y = sum(pts[:, 0])
        return (sum_x / length, sum_y / length)

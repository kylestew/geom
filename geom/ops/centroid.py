from geom.data.rectangle import Rectangle
from geom.data.circle import Circle
from geom.data.line import Line
from geom.data.polygon import Polygon
from geom.data.triangle import Triangle
from geom.data.point import Point

from geom.data.cube import Cube
from geom.data.sphere import Sphere

from numpy import sum
from geom.ops.point_at import point_at
from geom.ops.vertices import vertices

from shapely.geometry import Polygon as SPoly


def centroid(dat):
    """
    Computes centroid of given shape
    """
    if isinstance(dat, Point):
        return dat.pt

    if isinstance(dat, Rectangle):
        return dat.x + dat.w / 2.0, dat.y + dat.h / 2.0

    elif isinstance(dat, Circle):
        return dat.center

    elif isinstance(dat, Line):
        return point_at(dat, 0.5)

    elif isinstance(dat, Cube):
        return dat.center

    if isinstance(dat, Sphere):
        return dat.pos

    else:
        """
        https://stackoverflow.com/questions/23020659/fastest-way-to-calculate-the-centroid-of-a-set-of-coordinate-tuples-in-python-wi
        """
        pts = vertices(dat)
        length = pts.shape[0]
        sum_x = sum(pts[:, 0])
        sum_y = sum(pts[:, 0])
        return (sum_x / length, sum_y / length)

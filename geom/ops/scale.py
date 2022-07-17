from geom.data.rect import Rect
from geom.data.circle import Circle
from geom.data.line import Line
from geom.data.polygon import Polygon

from geom.ops.vertices import vertices
from geom.ops.centroid import centroid

from shapely.geometry import Polygon as SPolygon
from shapely import affinity


def _scale_points(pts, xscale, yscale):
    poly = SPolygon(pts)
    poly = affinity.scale(poly, xscale, yscale)
    return list(poly.exterior.coords)


def scale(dat, scale):
    """
    Scales given shape (origin of scale is center)
    (sx, sy) - scale multiplier for axis, 1.0 being no scale
    """
    (sx, sy) = scale

    if isinstance(dat, Rect):
        center = centroid(dat)
        scaled_size = (dat.size[0] * sx, dat.size[1] * sy)
        return Rect.from_center(center, scaled_size)

    elif isinstance(dat, Circle):
        raise Exception("NOT IMPLEMENTED")

    elif isinstance(dat, Line):
        raise Exception("NOT IMPLEMENTED")

    else:
        return Polygon(_scale_points(vertices(dat), sx, sy))

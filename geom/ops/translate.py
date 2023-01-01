from geom.data.circle import Circle
from geom.data.rect import Rect
from geom.data.polygon import Polygon

from geom.ops.vertices import vertices

from shapely.geometry import Polygon as SPolygon
from shapely import affinity

from numpy import array


def translate(dat, trans):
    """
    Translates the given data

    - (tx, ty): 2D translation amount
    """

    if isinstance(dat, Circle):
        return dat.with_center(dat.center + trans)

    if isinstance(dat, Rect):
        return dat.offset_by(trans)

    # treat all others as polys
    dx, dy = trans
    poly = SPolygon(vertices(dat))
    poly = affinity.translate(poly, dx, dy)
    pts = array(list(poly.exterior.coords))

    return Polygon(pts[:-1])

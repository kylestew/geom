from geom.data.polygon import Polygon
from .vertices import vertices


def as_polygon(dat):
    return Polygon(vertices(dat))

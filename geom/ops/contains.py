#%%
from geom.ops.vertices import vertices

from shapely.geometry import Polygon


def contains(dat, other):
    """
    Checks if given object fully contains another object
    (i.e. all points of a polygon lie within another polygon)
    """
    a = Polygon(vertices(dat))
    b = Polygon(vertices(other))
    return a.contains(b)

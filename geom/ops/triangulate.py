from geom.data.polygon import Polygon
from geom.ops.vertices import vertices

from shapely.geometry.polygon import Polygon as shp_polygon
from shapely.ops import triangulate as shp_triangulate


def triangulate(dat):
    verts = vertices(dat)
    polygon = shp_polygon(verts)
    s_polys = shp_triangulate(polygon)
    return [Polygon(list(poly.exterior.coords)) for poly in s_polys]

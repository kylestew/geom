from geom.data.polygon import Polygon
from geom.ops.vertices import vertices
from scipy.spatial import ConvexHull


def convex_hull(dat):
    verts = vertices(dat)
    hull = ConvexHull(verts)
    pts = verts[hull.vertices]
    return Polygon(pts)

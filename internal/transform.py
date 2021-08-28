from shapely.geometry import Polygon as SPolygon
from shapely import affinity
from numpy import array


def translate_points(pts, xoff, yoff):
    poly = SPolygon(pts)
    poly = affinity.translate(poly, xoff, yoff)
    return list(poly.exterior.coords)


def rotate_points(pts, rad):
    poly = SPolygon(pts)
    poly = affinity.rotate(poly, rad, origin="centroid", use_radians=True)
    pts = array(list(poly.exterior.coords))
    return pts[:-1]


def scale_points(pts, xscale, yscale):
    poly = SPolygon(pts)
    poly = affinity.scale(poly, xscale, yscale)
    return list(poly.exterior.coords)
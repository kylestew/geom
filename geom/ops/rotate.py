from geom.data.line import Line

from geom.ops.centroid import centroid

from math import cos, sin

from shapely.geometry import Polygon as SPolygon
from shapely.geometry import LineString as SLine
from shapely import affinity
from numpy import array


def rotate_points(pts, rad):
    poly = SPolygon(pts)
    poly = affinity.rotate(poly, rad, origin="centroid", use_radians=True)
    pts = array(list(poly.exterior.coords))
    return pts[:-1]


def rotate(dat, theta, center=None):
    """
    Rotates given data around specified center point
    (theta) - in radians, amount of rotation
    (center) - center of rotation (uses centroid if none specified)
    """

    # if isinstance(dat, Circle):
    #     return Circle(dat.origin, dat.r, dat.theta + theta)

    # if isinstance(dat, Rect):
    #     center = centroid(dat)
    #     scaled_size = (dat.size[0] * sx, dat.size[1] * sy)
    #     return Rect.from_center(center, scaled_size)

    if center == None:
        center = centroid(dat)

    # [a, b, d, e, xoff, yoff]
    # a = cos(-)
    # b = -sin(-)
    # d = sin(-)
    # e = cos(-)
    tx, ty = center
    # ident = [1, 0, 0, 0, 1, 0]
    trans = array([1, 0, 0, 1, tx, ty])
    rot = array([cos(theta), -sin(theta), sin(theta), cos(theta), 0, 0])
    untrans = array([1, 0, 0, 1, -tx, -ty])

    # TODO: what is rotation cooefficients
    # transform shit too

    if isinstance(dat, Line):
        line = SLine(dat.points)

        line = affinity.affine_transform(line, untrans)
        line = affinity.affine_transform(line, rot)
        line = affinity.affine_transform(line, trans)

        p0, p1 = list(line.coords)
        return Line(p0, p1)

    # else:
    # return Polygon(_scale_points(vertices(dat), sx, sy))

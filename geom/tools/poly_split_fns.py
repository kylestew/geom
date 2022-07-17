"""
TODO: move this into geom some day
"""
import numpy as np
from geom.data.rect import Rect
from geom.data.polygon import Polygon
from geom.data.triangle import Triangle
from geom.data.line import Line

from geom.ops.vertices import vertices
from geom.ops.split_at import split_at
from geom.ops.point_at import point_at


def tri_split(tri, pct):
    """
    splits a triangle in two along the line A-BC
    (so split line goes from first point through opposite midpoint)
    """
    if isinstance(tri, np.ndarray):
        [a, b, c] = tri
    else:
        [a, b, c] = tri.points

    line = Line(b, c)

    lines = split_at(line, pct)
    bc = lines[0].points[1]
    return np.array([Polygon((bc, a, b)), Polygon((bc, a, c))])


def tri_split_balanced(tri, pct):
    """
    finds the longest side and split the triangle at its midpoint
    """
    return tri_split(Triangle(tri.points).balanced(), pct)


def tri_split_mixed(tri):
    """
    Splits a triangle into a quad and two small triangles
    """
    # balance the triangle so we have stable points to work with
    balanced = Triangle.from_poly(tri).balanced()

    # find midpoints
    [a, b, c] = balanced.points
    ab = point_at(Line(a, b), 0.5)
    bc = point_at(Line(b, c), 0.5)
    ca = point_at(Line(c, a), 0.5)

    return np.array(
        [
            Polygon((a, ab, bc, ca)),
            Polygon((c, ca, bc)),
            Polygon((b, bc, ab)),
        ]
    )


def rect_split(rect: Rect, t: float, horiz=True):
    """Splits a rect horizontally or vertically at t

    Args:
        rect (geom.data.Rect): single rect to split
        t (float): pct to split at [0, 1]
        horiz (bool): split horizontally or vertically?

    Returns:
        list: a list of TWO rects
    """
    pos = (rect.x, rect.y)
    size = (rect.w, rect.h)
    if horiz:
        # horiz
        return np.array(
            [
                Rect(pos, (size[0] * t, size[1])),
                Rect(
                    (pos[0] + size[0] * t, pos[1]), (size[0] * (1 - t), size[1])
                ),
            ]
        )
    else:
        # vert
        t = 1 - t
        return np.array(
            [
                Rect(pos, (size[0], size[1] * t)),
                Rect(
                    (pos[0], pos[1] + size[1] * t), (size[0], size[1] * (1 - t))
                ),
            ]
        )


def rect_to_quad_rects(poly, pct=[0.5, 0.5]):
    """
    Subdivide a rectangle into 4 sections
    pct - center point to split on, (0.5, 0.5) is 4 equal rects from one
    """
    rect = Rect.wrapping_points(vertices(poly))

    a, b, c, d = vertices(rect)
    px, py = pct

    ab = point_at(Line(a, b), px)
    bc = point_at(Line(b, c), py)
    cd = point_at(Line(c, d), 1.0 - px)
    da = point_at(Line(d, a), 1.0 - py)

    return [
        Rect.wrapping_points((a, ab, da)),
        Rect.wrapping_points((ab, b, bc)),
        Rect.wrapping_points((bc, c, cd)),
        Rect.wrapping_points((cd, d, da)),
    ]


def rect_to_triangles(poly, flipped=False):
    [a, b, c, d] = vertices(poly)
    # triangle points define CCW
    if flipped:
        return np.array([Polygon((a, b, d)), Polygon((c, b, d))])
    else:
        return np.array([Polygon((b, c, a)), Polygon((d, a, c))])

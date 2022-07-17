from subprocess import call
from geom.data.rect import Rect
from geom.data.circle import Circle
from geom.data.polygon import Polygon
from geom.data.line import Line
import numpy as np


def draw(ctx, dat, attribs=None):
    # if an array of objects, run draw for each
    if isinstance(dat, np.ndarray) or type(dat) == list:
        for item in dat:
            draw(ctx, item, attribs=attribs)
        return

    # invoke attribs function if it exists
    attrs = dat.attribs if hasattr(dat, "attribs") else attribs

    if isinstance(dat, Rect):
        ctx.rect(dat.x, dat.y, dat.w, dat.h, attribs=attrs)

    elif isinstance(dat, Circle):
        x, y = dat.origin
        ctx.circle(x, y, dat.r, attribs=attrs)

    elif isinstance(dat, Polygon):
        ctx.path(dat.points.tolist(), closed=True, attribs=attrs)

    elif isinstance(dat, Line):
        p0, p1 = dat.points
        x0, y0 = p0
        x1, y1 = p1
        ctx.line(x0, y0, x1, y1, attribs=attrs)

    elif hasattr(dat, "points"):
        for pt in dat.points:
            ctx.point(pt, attribs=attrs)

    else:
        ctx.point(dat, attribs=attrs)

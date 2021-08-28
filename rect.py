from .polygon import Polygon
from .internal.resample import resample
from .internal.transform import translate_points, rotate_points, scale_points
from numpy import array


class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def as_polygon(self):
        return Polygon(self.vertices())

    def bounds(self):
        self

    def center(self):
        return self.x + self.w / 2.0, self.y + self.h / 2.0

    def edges(self):
        pass

    def resample(self, dist=None, num=None):
        return Polygon(resample(self.vertices(), dist, num))

    def translate(self, tx, ty):
        return Polygon(translate_points(self.vertices(), tx, ty))

    def rotate(self, rad):
        return Polygon(rotate_points(self.vertices(), rad))

    def scale(self, sx, sy):
        return Polygon(scale_points(self.vertices(), sx, sy))

    def vertices(self):
        p = (self.x, self.y)
        q = (p[0] + self.w, p[1] + self.h)
        return array([p, (q[0], p[1]), q, (p[0], q[1])])

    # === Cairo ===
    def draw(self, ctx, fill=False):
        ctx.rect(self.x, self.y, self.w, self.h, fill=fill)
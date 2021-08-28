from geom.api.shape import PCLike
from .internal.resample import resample
from numpy import array
from numpy.linalg import norm


class Line(PCLike):
    def __init__(self, a, b):
        super().__init__([a, b])

    # vector, position, and length to create line
    @classmethod
    def from_vector(cls, v, origin):
        a = origin
        b = origin + v
        return cls(a, b)

    # === Ops ===
    # area - ? (line has no area)
    # as_polygon - ?
    # bounds - ? (line has no bounds)

    def center(self):
        return self.point_at(0.5)

    def resample(self, dist=None, num=None):
        # TODO: does this become a polyline?
        return array(resample(self.vertices(), dist, num, closed=False))

    def _xys(self):
        p0, p1 = self.points
        x0, y0 = p0
        x1, y1 = p1
        return (x0, y0, x1, y1)

    def point_at(self, t):
        x0, y0, x1, y1 = self._xys()
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        return array((x, y))

    def split_at(self, t):
        p0, p1 = self.points
        p = self.point_at(t)
        return [Line(p0, p), Line(p, p1)]

    def shatter(self, ts):
        """
        split line at multiple t points [0, 1]
        method is going to behave weird if ts aren't in range [0, 1]
        """
        p_start, p_last = self.points
        segments = []
        for t in ts:
            p_end = self.point_at(t)
            segments.append(Line(p_start, p_end))
            p_start = p_end
        segments.append(Line(p_start, p_last))
        return segments

    def length(self):
        return norm(self.points)

    def as_vector(self):
        x0, y0, x1, y1 = self._xys()
        i = x1 - x0
        j = y1 - y0
        return array((i, j))

    def unit_vector(self):
        return self.as_vector() / self.length()

    def vertices(self):
        return self.points

    def draw(self, ctx):
        p0, p1 = self.points
        x0, y0 = p0
        x1, y1 = p1
        ctx.line(x0, y0, x1, y1)


"""
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
        poly = self.as_polygon()
        return Polygon(resample(poly.points, dist, num))

    def transform(self):
        pass

"""
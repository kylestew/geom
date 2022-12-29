from geom.api.apc import APC

from numpy import array
from numpy.linalg import norm


class Line(APC):
    def __init__(self, a=[0, 0], b=[1, 0]):
        """
        a: (x, y) start of line
        b: (x, y) end of line
        """
        super().__init__([a, b])

    def __str__(self):
        return "Line({0}, {1})".format(self.points[0], self.points[1])

    # vector, position, and length to create line
    @classmethod
    def from_vector(cls, v, origin):
        """
        v: (x, y) directional vector
        origin: (x, y) origin point of vector
        """
        a = origin
        b = origin + v
        return cls(a, b)

    # === Specialized ===
    def xys(self):
        p0, p1 = self.points
        x0, y0 = p0
        x1, y1 = p1
        return (x0, y0, x1, y1)

    def length(self):
        return norm(self.points)

    # treat Line as a vector
    def origin(self):
        return self.points[0]

    def direction(self):
        x0, y0, x1, y1 = self.xys()
        i = x1 - x0
        j = y1 - y0
        return array((i, j))

    def unit_vector(self):
        return self.direction() / self.length()

    def _point_at(self, t):
        x0, y0, x1, y1 = self.xys()
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        return array((x, y))

    def shatter(self, ts):
        """
        split line at multiple t points [0, 1]
        method is going to behave weird if ts aren't in range [0, 1]
        """
        p_start, p_last = self.points
        segments = []
        for t in ts:
            p_end = self._point_at(t)
            segments.append(Line(p_start, p_end))
            p_start = p_end
        segments.append(Line(p_start, p_last))
        return segments

# from .polygon import Polygon
# from .internal.resample import resample
# from .internal.transform import translate_points, rotate_points, scale_points
from .math.fit import fit01
from numpy import array
from math import cos, sin, pi, sqrt, atan2


class Arc:
    def __init__(self, cx=0, cy=0, r=1, start=0, end=2 * pi, clockwise=False):
        self.center = array((cx, cy))
        self.r = r
        self.start = start
        self.end = end
        self.clockwise = clockwise

    @classmethod
    def arcFrom2Points(cls, a, b, r, clockwise=False):
        # distance between two points
        x1, y1 = a
        x2, y2 = b
        # print("a", x1, y1)
        # print("b", x2, y2)
        dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        # print("dist", dist)
        # halfway point
        xAvg = (x1 + x2) / 2.0
        yAvg = (y1 + y2) / 2.0
        # print("mid", xAvg, yAvg)
        # circle center
        cx = sqrt(r * r - dist * dist / 4.0) * (y1 - y2) / dist
        cy = sqrt(r * r - dist * dist / 4.0) * (x2 - x1) / dist
        # cx = xAvg + (cx if clockwise else -cx)
        # cy = yAvg + (cy if clockwise else -cy)
        cx = xAvg + cx
        cy = yAvg + cy
        # print("center", cx, cy)
        # angles (cairo's arc and python's ATAN2 aren't friends)
        angle1 = -atan2(x1 - cx, y1 - cy) + pi / 2
        angle2 = -atan2(x2 - cx, y2 - cy) + pi / 2
        # print("constr arct", cx, cy, r, angle1, angle2)
        return cls(cx=cx, cy=cy, r=r, start=angle1, end=angle2, clockwise=clockwise)

    def point_at_theta(self, theta):
        cx, cy = self.center
        r = self.r
        return array([cx + r * cos(theta), cy + r * sin(theta)])

    def point_at(self, t):
        return self.point_at_theta(fit01(self.start, self.end, t))

    # === Cairo ===
    def draw(self, ctx, fill=False, closed=False):
        cx, cy = self.center
        if self.clockwise:
            ctx.arc(cx, cy, self.r, self.end, self.start, fill=fill, closed=closed)
        else:
            ctx.arc(cx, cy, self.r, self.start, self.end, fill=fill, closed=closed)


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
"""

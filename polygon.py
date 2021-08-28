from numpy import array
from geom.api.shape import PCLike
from .internal.resample import resample
from .internal.transform import translate_points, rotate_points, scale_points
from .line import Line


class Polygon(PCLike):
    def __init__(self, pts):
        super().__init__(pts)

    # === Ops ===
    def area(self):
        pass

    def as_polygon(self, n=None):
        return Polygon(self.vertices(n))

    def bounds(self):
        pass

    def center(self):
        pts = self.points
        area = 0
        xy = array([0.0, 0.0])
        a = pts[-1]
        for idx, pt in enumerate(pts):
            a = pts[idx - 1]
            z = a[0] * pt[1] - a[1] * pt[0]
            area += z
            xy += a + pt * z
        area = 1 / (area * 3)
        return xy * area

    def edges(self):
        lines = []
        for i0, pt in enumerate(self.points):
            i1 = i0 + 1
            if i1 >= len(self.points):
                i1 = 0
            p1 = self.points[i1]
            lines.append(Line(pt, p1))
        return array(lines)

    def resample(self, dist=None, num=None):
        return Polygon(resample(self.points, dist, num))

    # def tessellate(self, ?):

    def translate(self, tx, ty):
        return Polygon(translate_points(self.vertices(), tx, ty))

    def rotate(self, rad):
        return Polygon(rotate_points(self.vertices(), rad))

    def scale(self, sx, sy):
        return Polygon(scale_points(self.vertices(), sx, sy))

    def vertices(self, n=None):
        if n == None:
            return self.points

        # TODO: implement resampling
        return self.points

    # === Cairo ===
    def draw(self, ctx, fill=False):
        ctx.path(self.points.tolist(), closed=True, fill=fill)
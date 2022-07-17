from geom.api.shape import APC
from .internal.resample import resample
import numpy as np
import bezier


class Cubic(APC):
    def __init__(self, abcd):
        """
        abcd - 4 control points for cubic bezier spline
        """
        super().__init__(abcd)

    def __str__(self):
        return "Cubic({0}, {1}, {2}, {3})".format(
            self.points[0], self.points[1], self.points[2], self.points[3]
        )

    # === Ops ===
    def _curve(self):
        xs = self.points[:, 0]
        ys = self.points[:, 1]
        nodes = np.asfortranarray([xs, ys])
        return bezier.Curve(nodes, degree=3)

    def length(self):
        return self._curve().length

    def point_at(self, t):
        return self._curve().evaluate(t)

    def vertices(self):
        # sample cubic at pts
        pass
        # return self.points

    # === Cairo ===
    def draw(self, ctx, fill=False):
        [a, b, c, d] = self.points
        ctx.curve(a, b, c, d)

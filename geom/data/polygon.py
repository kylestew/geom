from geom.api.apc import APC

import numpy as np

from geom.data.line import Line


class Polygon(APC):
    def __init__(self, pts):
        super().__init__(pts)

    def __str__(self):
        return "Polygon({0})".format(self.points)

    # === Specialized ===

    @classmethod
    def quad_tris(cls):
        """
        creates and returns a quad made of two triangles
        """
        [a, b, c, d] = [
            [0, 0],
            [1, 0],
            [1, 1],
            [0, 1],
        ]
        return [
            Polygon((a, b, d)),
            Polygon((c, d, b)),
        ]

    def lines(self):
        pts = self.points
        pairs = np.stack((pts, np.roll(pts, -1, axis=0)), axis=1)

        lns = []
        for pair in pairs:
            a, b = pair
            lns.append(Line(a, b))

        return lns
from geom.api.apc import APC

import numpy as np

from geom.data.line import Line


class Polyline(APC):
    def __init__(self, pts):
        super().__init__(pts)

    def __str__(self):
        return "Polyline({0})".format(self.points)

    # === Specialized ===
    def lines(self):
        pts = self.points
        pairs = np.stack((pts, np.roll(pts, -1, axis=0)), axis=1)[0:-1]

        lns = []
        for pair in pairs:
            a, b = pair
            lns.append(Line(a, b))

        return lns

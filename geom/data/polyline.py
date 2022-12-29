from geom.api.apc import APC


class Polyline(APC):
    def __init__(self, pts):
        super().__init__(pts)

    def __str__(self):
        return "Polyline({0})".format(self.points)

    # === Specialized ===

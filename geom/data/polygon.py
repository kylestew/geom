from geom.api.apc import APC


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

    # def translate(self, tx, ty):
    #     return Polygon(translate_points(self.vertices(), tx, ty))

    # def rotate(self, rad):
    #     return Polygon(rotate_points(self.vertices(), rad))

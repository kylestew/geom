import numpy as np
from geom.data.polygon import Polygon
from scipy.spatial.distance import euclidean
from nil.nphacks import pair_bond


class Triangle(Polygon):
    def __init__(self, pts):
        super().__init__(pts)

    def __str__(self):
        return "Triangle({0}, {1}, {2})".format(
            self.points[0], self.points[1], self.points[2]
        )

    @classmethod
    def from_poly(cls, poly):
        return cls(poly.points[0:3])

    # === Specialized ===
    def balanced(self):
        """
        rotates the points in this triangle so that the longest side is defined by B-C
        """
        # find longest side
        # pair points, map to distances, and find index of longes distance
        largest_idx = np.argmax(
            np.array(
                [euclidean(a, b) for [a, b] in list(pair_bond(self.points))]
            )
        )

        # roll the triangle points into place
        # if 0 -> roll 1
        # if 1 -> don't roll
        # if 2 -> roll -1
        return Triangle(np.roll(self.points, (1 - largest_idx), axis=0))

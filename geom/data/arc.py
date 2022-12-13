#%%
from numpy import array
from math import pi


class Arc:
    def __init__(self, origin=[0, 0], r=1, theta=[0, pi]):
        """
        - origin [x, y]: center of arc
        - r [float]: radius of arc
        - theta [start, end]: beginning and ending angles to sweep
        """
        self.origin = array(origin)
        self.r = r
        self.theta = theta

    def __str__(self):
        return "Arc(({0}, {1}), r = {2}, theta: [{3}, {4}])".format(
            self.origin[0], self.origin[1], self.r, self.theta[0], self.theta[1]
        )

    def _repr_pretty_(self, p, cycle):
        p.text(str(self) if not cycle else "...")

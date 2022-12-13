from numpy import array


class Circle:
    def __init__(self, origin=[0, 0], r=1, theta=0):
        self.origin = array(origin)
        self.r = r
        self.theta = theta

    def __str__(self):
        return "Circle(({0}, {1}), r = {2})".format(
            self.origin[0], self.origin[1], self.r
        )

    def _repr_pretty_(self, p, cycle):
        p.text(str(self) if not cycle else "...")

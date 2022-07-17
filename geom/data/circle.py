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

    # def translate(self, tx, ty):
    #     pass

    # def rotate(self, rad):
    #     (
    #         x,
    #         y,
    #     ) = self.origin
    #     return Circle(x, y, self.r, self.theta + rad)

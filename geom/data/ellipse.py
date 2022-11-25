from numpy import array


class Ellipse:
    def __init__(self, origin=[0, 0], r=[1, 1], theta=0):
        self.origin = array(origin)
        self.r = r
        self.theta = theta

    def __str__(self):
        return "Ellipse(({0}, {1}), r = ({2}, {3}))".format(
            self.origin[0], self.origin[1], self.r[0], self.r[1]
        )

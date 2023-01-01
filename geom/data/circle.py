from numpy import array


class Circle:
    def __init__(self, center=[0, 0], r=1, theta=0):
        self.center = array(center)
        self.r = r
        self.theta = theta

    def __str__(self):
        return "Circle(({0}, {1}), r = {2})".format(
            self.center[0], self.center[1], self.r
        )

    def _repr_pretty_(self, p, cycle):
        p.text(str(self) if not cycle else "...")

    @classmethod
    def in_rect(cls, rect):
        """
        pos: (x, y) position of center of rect
        size: (width, height)
        """
        r = rect.w if rect.w < rect.h else rect.h
        r *= 0.5
        cent_x = rect.x + rect.w / 2.0
        cent_y = rect.y + rect.h / 2.0
        return cls((cent_x, cent_y), r)

    # === Specialized ===
    def with_center(self, center):
        return Circle(center, self.r, self.theta)

    def offset_by(self, offset):
        return self.with_center(self.center + offset)

    def with_radius(self, radius):
        return Circle(self.center, radius, self.theta)

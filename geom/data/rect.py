from .polygon import Polygon

from numpy import array, hsplit


class Rect(Polygon):
    def __init__(self, pos=[0, 0], size=[1, 1]):
        """
        pos: (x, y) position
        size: (width, height)
        """
        x, y = pos
        w, h = size
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pos = pos
        self.size = size

        # construct polygon
        p = (self.x, self.y)
        q = (p[0] + self.w, p[1] + self.h)
        verts = array([p, (q[0], p[1]), q, (p[0], q[1])])
        super().__init__(verts)

    def __str__(self):
        return "Rect(({0}, {1}), ({2}, {3}))".format(
            self.x, self.y, self.w, self.h
        )

    @classmethod
    def from_center(cls, pos, size):
        """
        pos: (x, y) position of center of rect
        size: (width, height)
        """
        x, y = pos
        w, h = size
        origin = [x - w / 2, y - h / 2]
        return cls(origin, size)

    @classmethod
    def from_bounds(cls, bounds):
        """
        bounds: (x, y, w, h)
        """
        x, y, w, h = bounds
        return cls((x, y), (w, h))

    @classmethod
    def wrapping_points(cls, pts):
        """
        given a list of points, determine a rect that contains all of them
        """
        # split xs and ys
        xs, ys = hsplit(array(pts), 2)

        xA = xs.min()
        xB = xs.max()
        yA = ys.min()
        yB = ys.max()

        pos = array((xA, yA))
        size = array((xB, yB)) - pos

        return cls(pos, size)

    # === Specialized ===
    def inset_by(self, amt):
        x = self.x + amt
        y = self.y + amt
        w = self.w - (amt * 2)
        h = self.h - (amt * 2)
        return Rect(pos=(x, y), size=(w, h))

    def offset_by(self, offset):
        """
        Offset position of rect

        - offset: (dx, dy)
        """
        dx, dy = offset
        x = self.x + dx
        y = self.y + dy
        return Rect(pos=(x, y), size=(self.w, self.h))

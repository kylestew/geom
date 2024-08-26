# %%
from typing import List
from .polygon import Polygon

from numpy import array, hsplit


class Rectangle(Polygon):
    def __init__(self, center=[0, 0], size=[1, 1]):
        """
        center: (x, y) origin position
        size: (width, height)
        """
        if len(center) != 2:
            raise ValueError("Position list must have exactly two elements.")
        if len(size) != 2:
            raise ValueError("Size list must have exactly two elements.")

        w, h = size
        pos = [center[0] - w / 2, center[1] - h / 2]
        x, y = pos

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pos = pos
        self.size = size

        # construct polygon
        p = (self.x, self.y)
        q = self.max
        verts = array([p, (q[0], p[1]), q, (p[0], q[1])])
        super().__init__(verts)

    def __str__(self):
        return "Rectangle(({0}, {1}), ({2}, {3}))".format(
            self.x, self.y, self.w, self.h
        )

    @property
    def center(self) -> List[float]:
        return [self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2]

    @property
    def max(self) -> List[float]:
        return [self.pos[0] + self.size[0], self.pos[1] + self.size[1]]

    # @classmethod
    # def from_bounds(cls, bounds):
    #     """
    #     bounds: (x, y, w, h)
    #     """
    #     x, y, w, h = bounds
    #     return cls((x, y), (w, h))

    # @classmethod
    # def wrapping_points(cls, pts):
    #     """
    #     given a list of points, determine a rect that contains all of them
    #     """
    #     # split xs and ys
    #     xs, ys = hsplit(array(pts), 2)

    #     xA = xs.min()
    #     xB = xs.max()
    #     yA = ys.min()
    #     yB = ys.max()

    #     pos = array((xA, yA))
    #     size = array((xB, yB)) - pos

    #     return cls(pos, size)

    # # === Specialized ===
    # def inset_by(self, amt):
    #     x = self.x + amt
    #     y = self.y + amt
    #     w = self.w - (amt * 2)
    #     h = self.h - (amt * 2)
    #     return Rect(pos=(x, y), size=(w, h))

    # def offset_by(self, offset):
    #     """
    #     Offset position of rect

    #     - offset: (dx, dy)
    #     """
    #     dx, dy = offset
    #     x = self.x + dx
    #     y = self.y + dy
    #     return Rect(pos=(x, y), size=(self.w, self.h))

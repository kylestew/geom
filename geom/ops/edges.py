from geom.data.rect import Rect
from geom.data.circle import Circle
from geom.data.line import Line
from numpy import array
from geom.ops.point_at import point_at

from numpy import repeat, roll, reshape


def _edges(vertices, closed=False):
    # pair off vertices and return
    # given: (A, B, C)
    # return: ((A, B), (B, C), (C, A))

    vert_count = len(vertices)
    # print(vert_count, vertices)
    pairs = repeat(vertices, 2, axis=0)
    # print(pairs)
    if closed == True:
        pairs = roll(pairs, -2)
    else:
        pairs = pairs[2:-2]

    # reshape back into paired vertices
    # TODO: this is not complete

    return pairs


def edges(dat):
    # def edges(self):
    #     return edges(self.vertices(), True)

    # OLD POLY IMPLEMENTATION
    # def edges(self):
    #     lines = []
    #     for i0, pt in enumerate(self.points):
    #         i1 = i0 + 1
    #         if i1 >= len(self.points):
    #             i1 = 0
    #         p1 = self.points[i1]
    #         lines.append(Line(pt, p1))
    #     return array(lines)

    pass

from geom.api.shape import PCLike

# from .rect import Rect
from numpy import linspace


class Grid(PCLike):
    def __init__(self, x, y, w, h, rows=10, cols=10, padding=0, offset=0):
        """
        (x, y) - top left of grid (origin)
        (w, h) - width, height of grid
        (rows, cols) - row, column count
        padding - (optional) inset the grid on all sides
        offset - (optional) offset every other row by a row span %
        """
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._rows = rows
        self._cols = cols

        s_x = x + padding
        s_y = y + padding
        i_w = w - padding * 2
        i_h = h - padding * 2
        e_x = s_x + i_w
        e_y = s_y + i_h
        span = i_w / cols
        row_a_offset = span * offset

        row_norm = linspace(s_x, e_x, cols + 1)
        row_offset = linspace(
            s_x + row_a_offset, e_x + row_a_offset, cols, endpoint=False
        )
        if offset <= 0 or offset >= 1:
            row_offset = row_norm
        ys = linspace(s_y, e_y, rows)

        pts = []
        for i, y in enumerate(ys):
            row = row_norm if i % 2 else row_offset
            for x in row:
                pts.append([x, y])

        super().__init__(pts)

    # === Helpers ===
    def centers(self):
        return self.points

    # === Ops ===
    def area(self):
        return self._w * self._h

    def bounds(self):
        pass

    # === Cairo ===
    def draw(self, ctx, px=1):
        for pt in self.points:
            x, y = pt
            ctx.point(x, y, px=px)

    # return list(map(lambda rect: rect.center(), self._cells))

    # def cells(self):
    # return self._cells

    # store the grid cells as rects
    # cw = (w - padding * (cols + 1)) / cols
    # ch = (h - padding * (rows + 1)) / rows

    # xs = linspace(0 + padding + x, w + x, cols, endpoint=False)
    # ys = linspace(0 + padding + y, h + y, rows, endpoint=False)

    # rects = []
    # for y in ys:
    # for x in xs:
    # r = Rect(x, y, cw, ch)
    # rects.append(r)

    #
    # self._cells = rects

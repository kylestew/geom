from geom.api.apc import APC

from numpy import linspace, array, meshgrid, stack


class Grid(APC):
    def __init__(self, x=0, y=0, w=1, h=1, rows=10, cols=10):
        """
        (x, y) - origin of grid
        (w, h) - width, height of grid
        (rows, cols) - row, column count
        returns:
        [[x, y]] positions for center points of grid cells
        """
        # store cell size for centering
        self.cell_size = array((w / cols, h / rows))

        # generate grid points, applying origin offset
        xs = linspace(0, w, cols, endpoint=False) + x
        ys = linspace(0, h, rows, endpoint=False) + y

        xx, yy = array(meshgrid(xs, ys, indexing="xy"))
        pts = stack((xx, yy), axis=2).reshape(-1, 2)

        self._x = x
        self._y = y
        self._w = w
        self._h = h

        super().__init__(pts)

    def __str__(self):
        return "Grid(({0}, {1}), ({2}, {3}))".format(
            self._x, self._y, self._w, self._h
        )

    def _repr_pretty_(self, p, cycle):
        p.text(str(self) if not cycle else "...")

    # === Specialized ===
    def centers(self):
        """
        By default, grid points are at origin of each cell
        This returns the center point of each cell instead
        """
        # apply centering and offset to each pt
        return self.points + self.cell_size / 2

    def cells(self):
        return array([[pt, pt + self.cell_size] for pt in self.points])

    def map(self, fn, from_centers=True):
        """
        Execute a function for each point in the grid and return
        the results
        """
        pts = self.centers() if from_centers == True else self.points
        return array([fn(pt, self.cell_size) for pt in pts])

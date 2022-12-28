from geom.api.apc import APC

from numpy import linspace, array, meshgrid, stack


class Grid(APC):
    def __init__(self, pos=[0, 0], size=[1, 1], grid=[10, 10]):
        """
        Creates a grid of evenly spaced positions.
        Grids increment like reading a page in a book (left/right, top/bottom).

        - pos: (x, y) bottom left origin of grid
        - size: (width, height) width and height of grid
        - grid: (rows, cols)

        returns:
        [[x, y]] positions for center points of grid cells
        """
        x, y = pos
        w, h = size
        rows, cols = grid

        # store cell size for centering
        self.cell_size = array((w / cols, h / rows))

        # generate grid points, applying origin offset
        # these positions are the top left of the grid cells
        xs = linspace(0, w, cols, endpoint=False) + x
        ys = linspace(0, h, rows, endpoint=False) + y

        xx, yy = array(meshgrid(xs, ys, indexing="xy"))
        pts = stack((xx, yy), axis=2).reshape(-1, 2)

        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self.rows = rows
        self.cols = cols

        self.cell_count = len(pts)

        super().__init__(pts)

    def __str__(self):
        return (
            "Grid(({0}, {1}), ({2}, {3}, rows: {4}, cols: {5}, cell_size: {6}))"
            .format(
                self._x,
                self._y,
                self._w,
                self._h,
                self.rows,
                self.cols,
                self.cell_size,
            )
        )

    # === Specialized ===
    def centers(self):
        """
        By default, grid points are at origin of each cell
        This returns the center point of each cell instead
        """
        # apply centering and offset to each pt
        return self.points + self.cell_size / 2

    def map(self, fn, from_centers=False):
        """
        Execute a function for each point in the grid and return
        the results as an array.

        - fn: (point, position) -> ()
            - point: (x, y)
            - position: (row, column)
        """
        pts = self.centers() if from_centers == True else self.points

        cols = self.cols
        return array(
            [fn(pt, (idx // cols, idx % cols)) for idx, pt in enumerate(pts)]
        )

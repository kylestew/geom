import numpy as np


class PCLike:
    def __init__(self, pts):
        if type(pts).__module__ == np.__name__:
            self.points = pts
        else:
            self.points = np.array(pts)

        assert self.points.ndim == 2, "Must be a 2d array"
        assert self.points.shape[1] == 2, "Array must contain [x, y] pairs"

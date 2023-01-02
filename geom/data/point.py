class Point:
    """
    Point:
    Useful if you want to attach attributes to a point
    """

    def __init__(self, pt=[0, 0]):
        self.pt = pt

    def __str__(self):
        x, y = self.pt
        return "Point({0, 1})".format(x, y)

    def _repr_pretty_(self, p, cycle):
        p.text(str(self) if not cycle else "...")

    # === Specialized ===
    @classmethod
    def to_points_array(cls, pts):
        """
        Converts a data array of points to an array of `Point` instances

        - pts: [(x, y)] array of points
        """
        return [cls(pt) for pt in pts]

    @classmethod
    def to_data_array(cls, points):
        """
        Converts an array of `Point` instances back to data

        - points: array of `Point` instances
        """
        return [point.pt for point in points]

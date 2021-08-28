from geom.api.shape import PCLike


class Polyline(PCLike):
    def __init__(self, pts):
        super().__init__(pts)
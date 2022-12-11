from geom.api.apc import APC


class Points(APC):
    def __str__(self):
        return "Points(num: {0})".format(len(self.points))

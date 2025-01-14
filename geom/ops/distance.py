from math import sqrt

from geom.ops.centroid import centroid

from geom.data.point import Point
from geom.data.line import Line


def distance(dat, pt):
    """
    Determines the distance between a given 'pt' and geom data object

    - dat: data.Geom object
    - pt: naked point array or Point object
    """
    # unwrap point if necessary
    if isinstance(pt, Point):
        px, py = pt.pt
    else:
        px, py = pt

    # if dat is a line, find distance to nearest point on line
    if isinstance(dat, Line):
        # Get line points
        x1, y1 = dat.points[0]
        x2, y2 = dat.points[1]

        # Calculate length of line squared
        line_length_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2

        if line_length_sq > 0:
            # Calculate projection parameter
            t = max(
                0,
                min(
                    1, ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / line_length_sq
                ),
            )

            # Find closest point on line segment
            proj_x = x1 + t * (x2 - x1)
            proj_y = y1 + t * (y2 - y1)

            # Return distance to closest point
            return sqrt((px - proj_x) ** 2 + (py - proj_y) ** 2)

    # else, find centroid of geometry and calculate distance to point
    x1, y1 = centroid(dat)
    return sqrt((px - x1) ** 2 + (py - y1) ** 2)

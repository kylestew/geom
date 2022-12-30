from numpy import roll, stack

from geom.data.line import Line
from geom.ops.vertices import vertices


def edges(dat, resample_count=12):
    """
    Converts shape to vertices and connects lines between
    each vertex pair. Returns that list of lines.
    """
    # convert shape to verts, use sample_count if shape can sample
    verts = vertices(dat, n=resample_count)

    # pair bond each vertex
    pairs = stack((verts, roll(verts, -1, axis=0)), axis=1)

    # return as lines
    return [Line(a, b) for a, b in pairs]

import pytest
import numpy as np
from numpy.testing import assert_array_equal

import geom.data as dat

from geom.ops import edges, vertices


def test_edges_polygon():
    poly = dat.Polygon(vertices(dat.Circle(), n=3))
    lines = edges(poly)

    assert len(lines) == 3

    # assert_array_equal(centroid(circ), [1, 2])

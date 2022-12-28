from numpy.testing import assert_array_equal, assert_almost_equal

import geom.data as dat
from geom.ops import vertices


def test_vertices_circle():
    circ = dat.Circle((1, 2), r=(3))
    assert_almost_equal(
        vertices(circ, n=3),
        [[4.0, 2.0], [-0.5, 4.598076], [-0.5, -0.598076]],
        decimal=3,
    )

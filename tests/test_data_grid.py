import numpy as np
from numpy.testing import assert_array_equal

from geom.data import Grid


def test_grid_create():
    grid = Grid(pos=[1, 2], size=[3, 2], grid=[2, 2])
    assert_array_equal(
        grid.points,
        [
            [1.0, 2.0],
            [2.5, 2.0],
            [1.0, 3.0],
            [2.5, 3.0],
        ],
    )
    assert_array_equal(grid.cell_size, [1.5, 1.0])


def test_grid_return_centers():
    grid = Grid(pos=[0, 0], size=[1.5, 2.0], grid=[2, 2])
    assert_array_equal(
        grid.centers(),
        [
            [0.375, 0.5],
            [1.125, 0.5],
            [0.375, 1.5],
            [1.125, 1.5],
        ],
    )


def test_grid_map_fn():
    grid = Grid(pos=[1, 2], size=[3, 2], grid=[2, 2])

    assert grid.cell_count == 4
    assert_array_equal(grid.cell_size, [1.5, 1.0])

    vals = grid.map(lambda idx, pt: [idx, pt])
    assert_array_equal(
        vals,
        [
            # idx, pt
            [0, np.array([1.0, 2.0])],
            [1, np.array([2.5, 2.0])],
            [2, np.array([1.0, 3.0])],
            [3, np.array([2.5, 3.0])],
        ],
    )


# def test_grid_map_fn_from_centers():
#     grid = Grid(size=[2, 2], grid=[2, 2])
#     vals = grid.map(lambda pt, sz: [pt, sz], from_centers=True)
#     assert_array_equal(
#         vals,
#         [
#             [[0.5, 0.5], [1.0, 1.0]],
#             [[1.5, 0.5], [1.0, 1.0]],
#             [[0.5, 1.5], [1.0, 1.0]],
#             [[1.5, 1.5], [1.0, 1.0]],
#         ],
#     )

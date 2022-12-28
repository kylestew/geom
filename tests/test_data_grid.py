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
    grid = Grid(pos=[1, 2], size=[3, 2], grid=[2, 3])

    assert grid.rows == 2
    assert grid.cols == 3
    assert grid.cell_count == 6
    assert_array_equal(grid.cell_size, [1.0, 1.0])

    vals = grid.map(lambda pt, pos: [pt[0], pt[1], pos[0], pos[1]])
    assert_array_equal(
        vals,
        [
            # x, y, row, column
            [1.0, 2.0, 0, 0],
            [2.0, 2.0, 0, 1],
            [3.0, 2.0, 0, 2],
            [1.0, 3.0, 1, 0],
            [2.0, 3.0, 1, 1],
            [3.0, 3.0, 1, 2],
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

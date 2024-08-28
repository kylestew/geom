from typing import List, Dict
from .types import Vec3
from .cube import Cube

from geom.ops.centroid import centroid


class CubeGrid:
    def __init__(self, center: Vec3, size: Vec3, rows: int, cols: int, layers: int):
        half_width = size[0] / 2
        half_height = size[1] / 2
        half_depth = size[2] / 2
        pos: Vec3 = (
            center[0] - half_width,
            center[1] - half_height,
            center[2] - half_depth,
        )

        self.pos = pos
        self.size = size
        self.rows = rows
        self.cols = cols
        self.layers = layers

    @classmethod
    def with_cube(cls, cube: Cube, rows: int, cols: int, layers: int):
        return cls(centroid(cube), cube.size, rows, cols, layers)

    @property
    def cell_count(self) -> int:
        return self.rows * self.cols * self.layers

    @property
    def cell_size(self) -> Vec3:
        return (
            self.size[0] / self.cols,
            self.size[1] / self.rows,
            self.size[2] / self.layers,
        )

    def centers(self) -> List[Vec3]:
        return [cell["center"] for cell in self.cells()]

    def cubes(self) -> List[Cube]:
        return [cell["cube"] for cell in self.cells()]

    def cells(self) -> List[Dict[str, any]]:
        cell_width, cell_height, cell_depth = self.cell_size

        cells: List[Dict[str, any]] = []
        index = 0
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(self.layers):
                    cx = self.pos[0] + j * cell_width + cell_width / 2
                    cy = self.pos[1] + i * cell_height + cell_height / 2
                    cz = self.pos[2] + k * cell_depth + cell_depth / 2

                    cube = Cube((cx, cy, cz), (cell_width, cell_height, cell_depth))
                    cells.append(
                        {
                            "index": index,
                            "t": index / self.cell_count,
                            "center": (cx, cy, cz),
                            "size": (cell_width, cell_height, cell_depth),
                            "row": i,
                            "col": j,
                            "layer": k,
                            "cube": cube,
                        }
                    )
                    index += 1
        return cells

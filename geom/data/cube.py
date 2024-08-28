from typing import List
from .rectangle import Rectangle


class Cube:
    """
    A class representing a 3D Cube shape.

    Attributes:
        pos (List[float]): The position of the Cube (origin at one corner).
        size (List[float]): The size of the Cube in 3D space.
        attribs (Dict[str, Any]): Optional attributes for the cube.
    """

    def __init__(self, center=[0, 0, 0], size=[1, 1, 1]):
        """
        center: (x, y, z) origin position
        size: (width, height, depth)
        """
        if len(center) != 3:
            raise ValueError("Position list must have exactly three elements.")
        if len(size) != 3:
            raise ValueError("Size list must have exactly three elements.")

        self.pos = [
            center[0] - size[0] / 2,
            center[1] - size[1] / 2,
            center[2] - size[2] / 2,
        ]
        self.size = size

    def __str__(self):
        return "Cube(({0}, {1}, {2}), ({3}, {4}, {5}))".format(
            self.pos[0],
            self.pos[1],
            self.pos[2],
            self.size[0],
            self.size[1],
            self.size[2],
        )

    @property
    def center(self) -> List[float]:
        return [
            self.pos[0] + self.size[0] / 2,
            self.pos[1] + self.size[1] / 2,
            self.pos[2] + self.size[2] / 2,
        ]

    @classmethod
    def with_rectangle(cls, rect: Rectangle, depth: float):
        pos = rect.center
        return cls([pos[0], pos[1], 0], [rect.size[0], rect.size[1], depth])

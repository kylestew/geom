from typing import List


class Sphere:
    """
    A class representing a sphere in 3D space. Meant to be converted to a mesh

    Args:
        center (list[float]): The center coordinates of the sphere. Default is [0, 0, 0].
        r (float): The radius of the sphere. Default is 1.0.
        subdivisions (int): The number of subdivisions for the sphere. Default is 2.
    """

    def __init__(self, center=[0, 0, 0], r=1.0, subdivisions=2):
        if len(center) != 3:
            raise ValueError("Position array must have exactly three elements.")
        if r <= 0:
            raise ValueError("Radius must be a positive number.")

        self.pos = center
        self.r = r
        self.subdivisions = subdivisions

    # @classmethod
    # def with_circle(cls, circle: Circle):
    #     center = centroid(circle)
    #     radius = circle.r

    #     # Create and return a new Sphere object using the circle's radius and calculated center
    #     return cls([center[0], center[1], 0], radius)

    # @classmethod
    # def inside_cube(cls, cube: Cube, subdivisions: int = 2):
    #     center = centroid(cube)
    #     radius = min(cube.size[0], cube.size[1], cube.size[2]) / 2

    #     return cls(center, radius, subdivisions)

    @property
    def center(self) -> List[float]:
        return self.pos

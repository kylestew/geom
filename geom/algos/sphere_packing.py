from geom.data.sphere import Sphere
from geom.ops.intersects import intersects


class SpherePacking:
    def __init__(self, obstacles=[]):
        self.obstacles = obstacles
        self.packed = []

    def attempt_placement(
        self, shape: Sphere, step_size: float = 0.1, max_size: float = 1.0
    ) -> Sphere:
        target_shape = shape
        placed_shape = None

        while all(
            not intersects(target_shape, other_shape)
            for other_shape in self.obstacles + self.packed
        ):
            placed_shape = target_shape

            if step_size is None:
                # if step_size is None, we don't want to increase the size of the shape
                break

            if target_shape.r >= max_size:
                break

            target_shape = Sphere(
                target_shape.pos,
                target_shape.r + step_size,
                target_shape.subdivisions,
            )

        if placed_shape is not None:
            self.packed.append(placed_shape)
            return placed_shape

        return None

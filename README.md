# GEOM

## A geometry data and functions library inspired by [thi.ng/geom](https://github.com/thi-ng/umbrella/tree/develop/packages/geom)

GEOM is split into multiple sub-packages

### DAT: `geom.data`

> A collection of data forward geometry shapes (rectangle, circle, polygon)

- Arc
- Circle
- Cubic
- Cube
- CubeGrid
- Ellipse
- Grid
- Line
- Point
- Polygon
- Polyline
- Rect
- Sphere
- Triangle

### OPS: `geom.ops`

> Functions that take data (from `geom.data`) and perform geometric related algorithms on them (i.e. resample, find bounds, etc)

- vertices
- as_polygon

- area
- bounds
- centroid
- contains
- convex_hull
- distance
- edges
- intersects
- point_at
- point_inside
- resample
- rotate
- scale
- scatter
- split_at
- translate
- triangulate

### MATH: `geom.math`

> Mathematical helper functions

- angle_to_unit_vector
- cart2pol
- fit01/fit10/fit11
- lerp
- make_normal
- norm
- remap
- rotate_point
- vector_perpendicular_to_vector

## Quick Start

```python
from geom.data import Circle, Point
from geom.ops import area, contains

# Create a circle
circle = Circle(Point(0, 0), radius=5)

# Calculate its area
circle_area = area(circle)

# Check if a point is inside
is_inside = contains(circle, Point(3, 3))
```

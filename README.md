# GEOM

## A geometry data and functions library inspired by [thi.ng/geom](https://github.com/thi-ng/umbrella/tree/develop/packages/geom)

GEOM is split into multiple sub-packages

### DAT: `geom.data`

> A collection of data forward geometry shapes (rectangle, circle, polygon)

- Arc
- Circle
- Cubic
- Ellipse
- Grid
- Line
- Point
- Polygon
- Rect
- Triangle


### OPS: `geom.ops`

> Functions that take data (from `geom.data`) and perform geometric related algorithms on them (i.e. resample, find bounds, etc)

- vertices
- as_polygon

- area
- bounds
- centroid

- contains
- point_at
- point_inside
- intersects

- rotate
- scale
- translate

- scatter

- resample
- split_at
- triangulate ???

- convex_hull ???
- edges ???


### MATH: `geom.math`

> Mathmatical helper functions

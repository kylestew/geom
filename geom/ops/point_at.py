from geom.data.line import Line
from numpy import array


def point_at(dat, t):
    """
    ???
    """
    if isinstance(dat, Line):
        x0, y0, x1, y1 = dat.xys()
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        return array((x, y))

    return None


"""
export const pointAt: MultiFn2<IShape, number, Vec | undefined> = defmulti<
    any,
    number,
    Vec | undefined
>(
    __dispatch,
    {
        quad: "poly",
        tri: "poly",
    },
    {
        arc: ($: Arc, t: number) => $.pointAtTheta(fit01(t, $.start, $.end)),

        circle: ($: Circle, t) => cartesian2(null, [$.r, TAU * t], $.pos),

        cubic: ({ points }: Cubic, t) =>
            mixCubic([], points[0], points[1], points[2], points[3], t),

        ellipse: ($: Ellipse, t) => madd2([], cossin(TAU * t), $.r, $.pos),

        line: ({ points }: Line, t) => mixN2([], points[0], points[1], t),

        poly: ($: Polygon, t) => new Sampler($.points, true).pointAt(t),

        polyline: ($: Polygon, t) => new Sampler($.points).pointAt(t),

        quadratic: ({ points }: Quadratic, t) =>
            mixQuadratic([], points[0], points[1], points[2], t),

        ray: ($: Ray, t) => pointOnRay2([], $.pos, $.dir, t),

        ray3: ($: Ray, t) => pointOnRay3([], $.pos, $.dir, t),

        rect: ($: Rect, t) => new Sampler(vertices($), true).pointAt(t),
    }
);
"""

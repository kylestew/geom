from geom.data.line import Line
from geom.ops.point_at import point_at
from numpy import array


def split_at(dat, t):
    """
    ???
    """
    if isinstance(dat, Line):
        p0, p1 = dat.points
        p = point_at(dat, t)
        return [Line(p0, p), Line(p, p1)]

    return None


"""
export const splitAt: MultiFn2<IShape, number, IShape[] | undefined> = defmulti<
    any,
    number,
    IShape[] | undefined
>(
    __dispatch,
    {},
    {
        arc: ($: Arc, t: number) => {
            const theta = fit01(t, $.start, $.end);
            return [
                new Arc(
                    set([], $.pos),
                    set([], $.r),
                    $.axis,
                    $.start,
                    theta,
                    $.xl,
                    $.cw,
                    __copyAttribs($)
                ),
                new Arc(
                    set([], $.pos),
                    set([], $.r),
                    $.axis,
                    theta,
                    $.end,
                    $.xl,
                    $.cw,
                    __copyAttribs($)
                ),
            ];
        },

        cubic: ({ attribs, points }: Cubic, t: number) =>
            cubicSplitAt(points[0], points[1], points[2], points[3], t).map(
                (pts) => new Cubic(pts, { ...attribs })
            ),

        line: ({ attribs, points }: Line, t) =>
            __splitLine(points[0], points[1], t).map(
                (pts) => new Line(pts, { ...attribs })
            ),

        polyline: ($: Polyline, t) =>
            __pointArraysAsShapes(
                Polyline,
                new Sampler($.points).splitAt(t),
                $.attribs
            ),

        quadratic: ({ attribs, points }: Quadratic, t: number) =>
            quadraticSplitAt(points[0], points[1], points[2], t).map(
                (pts) => new Quadratic(pts, { ...attribs })
            ),
    }
);
"""

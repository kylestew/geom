from geom.ops.vertices import vertices
from math import dist
from numpy import array
from numpy import append


def interpolate_pt(a, b, t):
    """
    Interpolate vector between A & B
    B*t+(1-t)*A

    a - [float, float]
        vector A
    b - [float, float]
        vector B
    t - float
        [0 - 1] parameter
    """
    A = array(a)
    B = array(b)
    return (B * t + (1 - t) * A).tolist()


def resample(data, dist=None, num=None, closed=False):
    pts = vertices(data)
    sampler = Sampler(pts, closed=closed)
    if dist:
        return sampler.sample_uniform(dist)
    elif num:
        return sampler.sample_fixed_num(num)
    return sampler.sample_fixed_num(20)


class Sampler:
    def __init__(self, pts, closed=False):
        """
        Note: closed means that it loops the points attaching last to first
        In the case of a line, you would want this to be false
        """
        if closed:
            self._pts = append(pts, [pts[0]], axis=0)
        else:
            self._pts = pts
        self.build_index(self._pts)

    def build_index(self, pts):
        """
        Build index of distance from first point for each point.
        """
        n = len(pts)
        idx = [0] * n
        i = 0
        j = 1
        while j < n:
            idx[j] = idx[i] + dist(pts[i], pts[j])
            i = j
            j += 1
        self._index = idx

    def total_length(self):
        idx = self._index
        return idx[-1] if len(idx) > 0 else 0

    def sample_uniform(self, dist):
        idx = self._index
        pts = self._pts
        total = self.total_length()
        delta = dist / total
        n = len(idx)

        result = []
        t = 0  # parameterized [0...1]
        i = 1
        while t <= 1.05:
            ct = t * total
            while ct >= idx[i] and i < n - 1:
                i += 1
            if i >= n:
                break
            p = idx[i - 1]

            c = interpolate_pt(pts[i - 1], pts[i], (ct - p) / (idx[i] - p))
            result.append(c)

            t += delta

        return result

    def sample_fixed_num(self, num):
        return self.sample_uniform(self.total_length() / (num - 1))

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


def resample(pts, dist=None, num=None, closed=True):
    sampler = Sampler(pts, closed=closed)
    if dist:
        return sampler.sample_uniform(dist)
    elif num:
        return sampler.sample_fixed_num(num)
    return sampler.sample_fixed_num(20)


class Sampler:
    def __init__(self, pts, closed=False):
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

    def sample_uniform(self, dist, includeLast=False):
        idx = self._index
        pts = self._pts
        total = self.total_length()
        delta = dist / total
        n = len(idx)

        result = []
        t = 0  # parameterized [0...1]
        i = 1
        while t < 1:
            ct = t * total
            while ct >= idx[i] and i < n:
                i += 1
            if i >= n:
                break
            p = idx[i - 1]

            c = interpolate_pt(pts[i - 1], pts[i], (ct - p) / (idx[i] - p))
            # print("interpolate", pts[i - 1], pts[i], (ct - p) / (idx[i] - p), c)
            result.append(c)

            t += delta

        return result
        # return result[:-1]

    def sample_fixed_num(self, num, includeLast=False):
        return self.sample_uniform(self.total_length() / num, includeLast)

from .interval import clamp01, clamp11


def fit01(a, b, t):
    return a + (b - a) * clamp01(t)


def fit10(a, b, t):
    return b + (a - b) * clamp01(t)


def fit11(a, b, t):
    return a + (b - a) * (0.5 + 0.5 * clamp11(t))
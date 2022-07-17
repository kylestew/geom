def clamp01(x):
    """
    Clamps value 'x' to closed [0 .. 1] interval
    """
    if x < 0:
        return 0
    elif x > 1:
        return 1
    return x


def clamp11(x):
    """
    Clamps value 'x' to closed [-1 .. 1] interval
    """
    if x < -1:
        return -1
    elif x > 1:
        return 1
    return x
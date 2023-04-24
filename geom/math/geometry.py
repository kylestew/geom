import numpy as np


def angle_to_unit_vector(theta):
    return make_normal(np.append(np.cos(theta), np.sin(theta)))

def vector_perpendicular_to_vector(v, clockwise=True):
    if clockwise:
        return norm((v[1], -v[0]))
    else:
        return norm((-v[1], v[0]))

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return (rho, phi)

def norm(v):
    return v / np.linalg.norm(v)

def make_normal(p, orig=np.array([0, 0])):
    v = np.array(p) - orig
    return v / np.linalg.norm(v)


def rotate_point(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    import math

    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

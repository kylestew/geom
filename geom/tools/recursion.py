from iteration_utilities import deepflatten
from geom.ops.area import area


def randomized_base_case(depth, min_depth, max_depth, random_fn):
    if depth < min_depth:
        return False
    if depth == max_depth:
        return True
    else:
        return random_fn()


def _recursive_subdiv(poly, subdiv_poly_fn, hit_base_case_fn, depth=0):
    if hit_base_case_fn(depth):
        return poly
    else:
        polys = subdiv_poly_fn(poly, depth)
        results = [
            _recursive_subdiv(poly, subdiv_poly_fn, hit_base_case_fn, depth + 1)
            for poly in polys
        ]
        return results


def recursive_subdiv(poly, subdiv_poly_fn, hit_base_case_fn):
    return list(
        deepflatten(
            _recursive_subdiv(poly, subdiv_poly_fn, hit_base_case_fn, 0)
        )
    )


def _balanced_recursive_subdiv(poly, subdiv_poly_fn, hit_base_case_fn, depth=0):
    if hit_base_case_fn(depth):
        return poly
    else:
        polys = subdiv_poly_fn(poly, depth)
        # decide which poly has the largest area
        sorted_poly_areas = sorted(
            [(area(poly), poly) for poly in polys], key=lambda x: x[0]
        )
        to_subdivide = sorted_poly_areas.pop()[1]
        # recurse only on that poly
        results = _recursive_subdiv(
            to_subdivide, subdiv_poly_fn, hit_base_case_fn, depth + 1
        )
        # combine with current generation results that stopped recursion
        return [results, [x[1] for x in sorted_poly_areas]]


def balanced_recursive_subdiv(poly, subdiv_poly_fn, hit_base_case_fn):
    """
    Only performs recursion on the generations output that hass the largest area.
    Tends to keep the recursion more stable

    Args:
        poly (geom.data): single poly to split into the next generation
        subdiv_poly_fn (fn): a function that takes a single `poly` and `depth` integer, returns one or more polygons
        hit_base_case_fn (fn): a function that determines if the bases cases hass been it, takes `depth` integer

    Returns:
        list: flattened list of all recursive generational output
    """
    return list(
        deepflatten(
            _balanced_recursive_subdiv(
                poly, subdiv_poly_fn, hit_base_case_fn, 0
            )
        )
    )

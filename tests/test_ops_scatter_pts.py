import pytest
import numpy as np

import geom.data as dat

from geom.ops import scatter, RandomSampling


def test_scatter_pts_random():
    circ = dat.Circle((1, 1), r=1)
    pts = scatter(circ, num=128, sampling=RandomSampling.RANDOM)
    assert len(pts) == 128


def test_scatter_pts_uniform():
    circ = dat.Rectangle()
    pts = scatter(circ, num=128, sampling=RandomSampling.UNIFORM)
    assert len(pts) == 128


def test_scatter_pts_gaussian():
    circ = dat.Rectangle()
    pts = scatter(circ, num=128, sampling=RandomSampling.GAUSSIAN)
    assert len(pts) == 128

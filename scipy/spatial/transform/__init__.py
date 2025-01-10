"""
Spatial Transformations (:mod:`scipy.spatial.transform`)
========================================================

.. currentmodule:: scipy.spatial.transform

This package implements various spatial transformations. For now,
rotations and rigid transformations (rotations and translations) are
supported.

Rotations in 3 dimensions
-------------------------
.. autosummary::
   :toctree: generated/

   RigidTransformation
   Rotation
   Slerp
   RotationSpline
"""
from ._rigidtransformation import RigidTransformation
from ._rotation import Rotation, Slerp
from ._rotation_spline import RotationSpline

# Deprecated namespaces, to be removed in v2.0.0
from . import rotation

__all__ = ['Rotation', 'Slerp', 'RotationSpline', 'RigidTransformation']

from scipy._lib._testutils import PytestTester
test = PytestTester(__name__)
del PytestTester

"""Example module: the simple harmonic oscillator.

This file is a placeholder. Replace it with your own code. It exists so that
the tests and the CI pipeline have something real to run on day one.

The system is x'' = -omega**2 * x, with unit mass.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


def _check_omega(omega: float) -> None:
    if omega <= 0:
        raise ValueError("omega must be positive")


def exact_solution(
    t: ArrayLike, x0: float, v0: float, omega: float
) -> NDArray[np.float64]:
    """Return the exact position x(t) for initial conditions (x0, v0)."""
    _check_omega(omega)
    t = np.asarray(t, dtype=float)
    return x0 * np.cos(omega * t) + (v0 / omega) * np.sin(omega * t)


def exact_velocity(
    t: ArrayLike, x0: float, v0: float, omega: float
) -> NDArray[np.float64]:
    """Return the exact velocity v(t) for initial conditions (x0, v0)."""
    _check_omega(omega)
    t = np.asarray(t, dtype=float)
    return -x0 * omega * np.sin(omega * t) + v0 * np.cos(omega * t)


def energy(x: ArrayLike, v: ArrayLike, omega: float) -> NDArray[np.float64]:
    """Return the total energy per unit mass, E = (v**2 + omega**2 x**2) / 2."""
    _check_omega(omega)
    x = np.asarray(x, dtype=float)
    v = np.asarray(v, dtype=float)
    return 0.5 * (v**2 + (omega * x) ** 2)

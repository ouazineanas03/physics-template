import numpy as np
import pytest

from physproj import energy, exact_solution, exact_velocity

OMEGA = 2.0
X0, V0 = 1.0, 0.5


def test_initial_conditions_are_respected():
    assert exact_solution(0.0, X0, V0, OMEGA) == pytest.approx(X0)
    assert exact_velocity(0.0, X0, V0, OMEGA) == pytest.approx(V0)


def test_energy_is_conserved_along_the_exact_solution():
    t = np.linspace(0.0, 10.0, 200)
    x = exact_solution(t, X0, V0, OMEGA)
    v = exact_velocity(t, X0, V0, OMEGA)
    e = energy(x, v, OMEGA)
    assert np.allclose(e, e[0], rtol=1e-12)


def test_period_is_two_pi_over_omega():
    period = 2 * np.pi / OMEGA
    assert exact_solution(period, X0, V0, OMEGA) == pytest.approx(X0)


@pytest.mark.parametrize("omega", [0.0, -1.0])
def test_non_positive_omega_is_rejected(omega):
    with pytest.raises(ValueError):
        exact_solution(1.0, X0, V0, omega)

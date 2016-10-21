import numpy as np

from scipy.integrate import odeint


def van_der_pol(eps):
    """Returns a function that defines a van Der Pol oscillator's ODE."""
    def diff_eq(func, time):
        """The van Der Pol ODE."""
        var_x = func[0]  # dx/dt
        var_y = func[1]  # d^2x/dt^2

        return [var_y, -var_x + eps * (1 - var_x**2) * var_y]
    return diff_eq


def solve_van_der_pol(eps, x_init, time):
    """ Solves the van der pol ODE

    eps - The damping coefficient.
    x_0 - The initial conditions.
    t   - The time axis.
    """

    return odeint(van_der_pol(eps), x_init, time)


# Variation in initial conditions
def solve_no_init():
    """Solves van Der Pol's equation for the case with no initial
    conditions."""

    time = np.linspace(0, 10, 100e-3)  # For 100 FPS animation.
    x_init = [0, 0]
    eps = 0
    return solve_van_der_pol(eps, x_init, time)


def solve_first_0():
    """Solves van Der Pol's equation for the case with first initial
    condition as zero."""

    time = np.linspace(0, 10, 100e-3)  # For 100 FPS animation.
    x_init = [0, 1]
    eps = 0
    return solve_van_der_pol(eps, x_init, time)


def solve_second_0():
    """Solves van Der Pol's equation for the case with second initial
    condition as zero."""

    time = np.linspace(0, 10, 100e-3)  # For 100 FPS animation.
    x_init = [1, 0]
    eps = 0
    return solve_van_der_pol(eps, x_init, time)


def solve_both_nonzero():
    """Solves van Der Pol's equation for the case with both initial
    conditions as non-zero."""

    time = np.linspace(0, 10, 100e-3)  # For 100 FPS animation.
    x_init = [1, 1]
    eps = 0
    return solve_van_der_pol(eps, x_init, time)


# Variation in eps
def solve_eps_0():
    """Solves the van Der Pol ODE for epsilon = 0."""

    time = np.linspace(0, 10, 100e-3)  # For 100 FPS animation.
    x_init = [1, 1]
    eps = 0
    return solve_van_der_pol(eps, x_init, time)


def solve_eps_0_1():
    """Solves the van Der Pol ODE for epsilon = 0.5 (i.e. between 0
    and 1)."""

    time = np.linspace(0, 10, 100e-3)  # For 100 FPS animation.
    x_init = [1, 1]
    eps = 0.5
    return solve_van_der_pol(eps, x_init, time)


def solve_eps_1():
    """Solves the van Der Pol ODE for epsilon = 1."""

    time = np.linspace(0, 10, 100e-3)  # For 100 FPS animation.
    x_init = [1, 1]
    eps = 1
    return solve_van_der_pol(eps, x_init, time)


def solve_eps_5():
    """Solves the van Der Pol ODE for epsilon = 5. (i.e. greater than
    1)"""

    time = np.linspace(0, 10, 100e-3)  # For 100 FPS animation.
    x_init = [1, 1]
    eps = 5
    return solve_van_der_pol(eps, x_init, time)

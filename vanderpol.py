from scipy.integrate import odeint

import numpy as np

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



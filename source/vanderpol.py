#!/bin/python3.5

import matplotlib.animation as manimation
import matplotlib.pyplot as plt

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

    time = np.arange(0, 40, 100e-3)
    x_init = [0, 0]
    eps = 0
    return (time, solve_van_der_pol(eps, x_init, time))


def solve_first_0():
    """Solves van Der Pol's equation for the case with first initial
    condition as zero."""

    time = np.arange(0, 40, 100e-3)
    x_init = [0, 1]
    eps = 0
    return (time, solve_van_der_pol(eps, x_init, time))


def solve_second_0():
    """Solves van Der Pol's equation for the case with second initial
    condition as zero."""

    time = np.arange(0, 40, 100e-3)
    x_init = [1, 0]
    eps = 0
    return (time, solve_van_der_pol(eps, x_init, time))


def solve_both_nonzero():
    """Solves van Der Pol's equation for the case with both initial
    conditions as non-zero."""

    time = np.arange(0, 40, 100e-3)
    x_init = [1, 1]
    eps = 0
    return (time, solve_van_der_pol(eps, x_init, time))


# Variation in eps
def solve_eps_0():
    """Solves the van Der Pol ODE for epsilon = 0."""

    time = np.arange(0, 40, 100e-3)
    x_init = [1, 1]
    eps = 0
    return (time, solve_van_der_pol(eps, x_init, time))


def solve_eps_0_1():
    """Solves the van Der Pol ODE for epsilon = 0.5 (i.e. between 0
    and 1)."""

    time = np.arange(0, 40, 100e-3)
    x_init = [1, 1]
    eps = 0.5
    return (time, solve_van_der_pol(eps, x_init, time))


def solve_eps_1():
    """Solves the van Der Pol ODE for epsilon = 1."""

    time = np.arange(0, 40, 100e-3)
    x_init = [1, 1]
    eps = 1
    return (time, solve_van_der_pol(eps, x_init, time))


def solve_eps_5():
    """Solves the van Der Pol ODE for epsilon = 5. (i.e. greater than
    1)"""

    time = np.arange(0, 40, 100e-3)
    x_init = [1, 1]
    eps = 5
    return (time, solve_van_der_pol(eps, x_init, time))


class GlobalPlotParams:
    xlabel_font = {}
    ylabel_font = {}
    linewidth = 1
    fig_size = (8.0, 6.0)
    markers = ['o', '^', 's', 'p', 'x', 'D', '|', '*']
    colors = ['red', 'blue', 'green', 'black', 'magenta']
    ftype = 'eps'
    font_size = 12


# Plot generator function.
def gen_plt(solve_funcs, title, xlabel, ylabel, legend, out_file):
    plt.figure(figsize=GlobalPlotParams.fig_size)

    for func, marker, color in zip(solve_funcs,
                                   GlobalPlotParams.markers,
                                   GlobalPlotParams.colors):
        time, data = func()
        plt.plot(time, data[:, 0], marker=marker, color=color,
                 linewidth=GlobalPlotParams.linewidth)

    plt.legend(legend, loc='best', fontsize=GlobalPlotParams.font_size)
    plt.title(title, fontsize=GlobalPlotParams.font_size)
    plt.xlabel(xlabel, fontsize=GlobalPlotParams.font_size)
    plt.ylabel(ylabel, fontsize=GlobalPlotParams.font_size)
    plt.tight_layout()
    plt.savefig(out_file, format=GlobalPlotParams.ftype)


# Generate plot showing variation in initial conditions.
def gen_plts_init_cond():
    ode_cases = [solve_no_init, solve_first_0, solve_second_0,
                 solve_both_nonzero]

    legend = ["Zero initial conditions",
              "Initial Conditions: $x = 0$, $\dot{x} = 1$",
              "Initial Conditions: $x = 1$, $\dot{x} = 0$",
              "Initial Conditions: $x = 1$, $\dot{x} = 1$"]

    gen_plt(solve_funcs=ode_cases,
            title="Variation of Initial Conditions",
            xlabel="Time",
            ylabel="Amplitude",
            legend=legend,
            out_file="../output/van_der_pol_init.eps")


# Generate plot showing variation in damping factor.
def gen_plt_eps_var():
    ode_cases = [solve_eps_0, solve_eps_0_1,
                 solve_eps_1, solve_eps_5]

    legend = ["Damping Factor: $\epsilon = 0$",
              "Damping Factor: $\epsilon = 0.5$",
              "Damping Factor: $\epsilon = 1$",
              "Damping Factor: $\epsilon = 5$"]

    gen_plt(ode_cases, "Variation of Damping Factor", "Time",
            "Amplitude", legend, "../output/van_der_pol_eps.eps")


# Generate plots for all the cases above
def gen_all_plots():
    gen_plts_init_cond()
    gen_plt_eps_var()


def gen_video(filename):
    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='van Der Pol Oscillator', artist='Matplotlib',
                    comment="An animation of the van Der Pol\
                    oscillator's amplitude with time.")
    writer = FFMpegWriter(fps=60, metadata=metadata, codec='libtheora')

    eps = 2
    x_init = [1, 1]
    time = np.arange(0, 40, 100e-3)
    amp = solve_van_der_pol(eps, x_init, time)[:, 0]

    fig = plt.figure(figsize=(19.20, 10.80))

    with writer.saving(fig, filename, 100):
        for idx in range(len(time)):
            plt.cla()
            plt.xlim(0, 40)
            plt.ylim(amp.min() - 1, amp.max() + 1)
            plt.xlabel('Time (seconds)', fontsize=20)
            plt.ylabel('Amplitude', fontsize=25)
            plt.title('van Der Pol Oscillator (Animation at 6x Speed)',
                      fontsize=20)
            plt.plot(time[idx], amp[idx], 'bo')
            plt.plot(time[:idx], amp[:idx], linewidth=2, color='blue')
            plt.grid()
            writer.grab_frame()


if __name__ == '__main__':
    gen_all_plots()
    gen_video('../output/animation.ogg')
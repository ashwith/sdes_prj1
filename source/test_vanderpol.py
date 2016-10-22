import numpy as np

import pytest

import vanderpol as vdp


class TestVanDerPol:
    def test_ret_type(self):
        assert callable(vdp.van_der_pol(5))

    def test_ret_len(self):
        eps = 5
        x_init = [0, 1]
        time = 1
        func = vdp.van_der_pol(eps)
        assert len(func(x_init, time)) == 2

    def test_ret_dat(self):
        eps = 5
        x_init = [0, 1]
        time = 1
        func = vdp.van_der_pol(eps)
        assert func(x_init, time) ==\
            [x_init[1],
             -x_init[0] + eps * (1 - x_init[0] * x_init[0]) * x_init[1]]


class TestSolveVanDerPol:
    def test_ret_type(self):
        eps = 5
        x_init = [0, 1]
        time = 1
        assert type(vdp.solve_van_der_pol(eps, x_init, time)) == np.ndarray

    def test_ret_len(self):
        eps = 5
        x_init = [0, 1]
        time = 1
        assert len(vdp.solve_van_der_pol(eps, x_init, time)) == 1


class TestSolutions:

    def test_solvers(self):
        func_list = [vdp.solve_no_init,
                     vdp.solve_first_0,
                     vdp.solve_second_0,
                     vdp.solve_both_nonzero_equal,
                     vdp.solve_both_nonzero_unequal,
                     vdp.solve_eps_0,
                     vdp.solve_eps_0_1,
                     vdp.solve_eps_1,
                     vdp.solve_eps_5]

        for func in func_list:
            ret = func()
            assert len(ret) == 2
            assert type(ret[0]) == np.ndarray
            assert type(ret[1]) == np.ndarray
            assert len(ret[0]) == len(ret[1])
            assert np.shape(ret[1]) == (len(ret[0]), 2)

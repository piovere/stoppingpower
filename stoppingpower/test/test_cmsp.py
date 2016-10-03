import unittest
import numpy as np
from stoppingpower.cmsp import *


class test_collisional_mass_stopping_power(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def percent_errror(self, truth, guess):
        # Error for the project is 3-5%
        self.max_error = 0.03
        return np.abs(truth - guess) / truth

    def almost(self, truth, guess):
        self.assertLessEqual(
            self.percent_errror(truth, guess),
            self.max_error,
            msg="{0} is not close to {1}".format(truth, guess)
        )

    def test_basic_CMSP_calculation(self):
        # I have a batch of values to test
        self.almost(21.75, normal_S_c(1.0, 10.0, 25.0, 1.0, 75.0, 18.0))
        self.almost(423.0, normal_S_c(14.0, 13.0, 500.0 * 28, 28.085, 166, 26.9815385))


if __name__ == "__main__":
    unittest.main()

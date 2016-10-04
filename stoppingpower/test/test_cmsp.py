import unittest
from stoppingpower.cmsp import *
from stoppingpower.materials import materials
from stoppingpower.range import rangeout


class test_collisional_mass_stopping_power(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def percent_errror(self, truth, guess):
        # Error for the project is 3-5%
        self.max_error = 0.05
        return np.abs(truth - guess) / truth

    def almost(self, truth, guess):
        """

        :rtype: NoneType
        """
        self.assertLessEqual(
            self.percent_errror(truth, guess),
            self.max_error,
            msg="{0} is not close to {1}".format(truth, guess)
        )

    def test_basic_CMSP_calculation(self):
        # I have a batch of values to test
        self.almost(21.75, normal_S_c(1.0, 10.0, 25.0, 1.0, 75.0, 18.0))
        self.almost(423.0, normal_S_c(14.0, 13.0, 500.0 * 28.0, 27.977, 166.0, 26.9815385))

    def test_CMSP_with_complex_material(self):
        # Let's try water again
        self.almost(21.75, S_c(1.0, materials.get("Water"), 25.0, 1.0))
        # Now for concrete
        self.almost(216.8, S_c(6.0, materials.get("Concrete"), 1200.0, 12.0))
        # 10.0 MeV alpha in Air
        self.almost(463.7, S_c(2.0, materials.get("Air"), 10.0, 4.001506466))
        # 330 MeV/nucleon Fe (Z=26, A=56) in Lead
        self.almost(1147.0, S_c(26.0, materials.get("Lead, 82"), 330.0 * 56.0, 56.0))

    def test_range(self):
        # 45 MeV proton in water
        self.almost(1.841, rangeout(1.0, materials.get("Water"), 45.0, 1.0))
        # 600 MeV Carbon in Lead
        self.almost(0.151, rangeout(6.0, materials.get("Lead, 82"), 600.0, 12.0))
        # 500 MeV/nucleon Ar (Z=18, A=40) in concrete
        self.almost(7.06, rangeout(18.0, materials.get("Concrete"), 500.0 * 40.0, 39.948))
        # 20 MeV proton in air
        self.almost(403.0, rangeout(1.0, materials.get("Air"), 20.0, 1.0))
        # 200 MeV/nucleon Ne (Z=10, A=20) in Aluminum
        self.almost(2.493, rangeout(10.0, materials.get("Aluminum, 13"), 200.0 * 20.0, 20.0))


if __name__ == "__main__":
    unittest.main()

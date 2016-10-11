from unittest import TestCase
from stoppingpower.geometric import microscopic_cross_section
from stoppingpower.range import nuclear_fraction
from stoppingpower.materials import materials
import logging
import numpy as np


class TestGeometric(TestCase):
    def setUp(self):
        logging.basicConfig(filename='example.log',level=logging.ERROR)

    def test_cross_section_against_homework_3(self):
        """ Compares two values from class homework 3-1
        """
        a1 = 4.0
        a2 = 12.0
        test = microscopic_cross_section(a1, a2)
        real = 0.925
        self.assertAlmostEqual(test, real, places=3)

        a3 = 1.0
        a4 = 4.0
        test = microscopic_cross_section(a3, a4)
        real = 0.412
        self.assertAlmostEqual(test, real, places=3)

    def percent_errror(self, truth, guess):
        # Error for the project is 3-5%
        self.max_error = 0.05
        return np.abs(truth - guess) / truth

    def almost(self, truth, guess):
        """

        :rtype: NoneType
        """
        PE = (truth - guess) / truth

        if abs(PE) <= 0.05:
            logging.info("{0}\t\t\t{1}\t\t\t{2}".format(truth, guess, PE))
        else:
            logging.warning("{0}\t\t\t{1}\t\t\t{2}".format(truth, guess, PE))

        self.assertLessEqual(
            self.percent_errror(truth, guess),
            self.max_error,
            msg="{0} is not close to {1}".format(truth, guess)
        )

    def test_fraction_undergoing_nuclear_reaction_600_mev_per_nucleon_oxygen_through_1_cm_al(self):
        logging.info("3.a.iii Nuclear Fraction: 600 MeV/nucleon Oxygen (Z=8, A=16) through 1cm Aluminum")
        self.almost(0.107, nuclear_fraction(16.0, materials.get("Aluminum, 13"), 1.0))

    def test_fraction_undergoing_nuclear_reaction_500_mev_proton_through_8_mm_pb(self):
        logging.info("3.b.iii Nuclear Fraction: 500 MeV proton through 8mm of lead")
        self.almost(0.075, nuclear_fraction(1.0, materials.get("Lead, 82"), 0.8))

    def test_fraction_undergoing_nuclear_reaction_430_mev_per_nucleon_nitrogen_through_2_cm_concrete(self):
        logging.info("3.c.iii Nuclear Fraction: 430 MeV/nucleon Nitrogen (Z=7, A=14) through 2cm concrete")
        self.almost(0.212, nuclear_fraction(14.0, materials.get("Concrete"), 2.0))

    def test_fraction_undergoing_nuclear_reaction_260_mev_per_nucleon_alpha_through_4_cm_water(self):
        logging.info("3.d.iii Nuclear Fraction: 260 MeV/nucleon alpha through 4 cm water")
        self.almost(0.221, nuclear_fraction(4.0, materials.get("Water"), 4.0))

    def test_fraction_undergoing_nuclear_reaction_800_mev_proton_through_1_km_air(self):
        logging.info("3.e.iii Nuclear Fraction: 800 MeV proton through 1km air")
        self.almost(0.974, nuclear_fraction(1.0, materials.get("Air"), 100000.0))

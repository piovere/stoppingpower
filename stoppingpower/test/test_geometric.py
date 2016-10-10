from unittest import TestCase
from stoppingpower.geometric import cross_section


class TestGeometric(TestCase):
    def test_cross_section_against_homework_3(self):
        """ Compares two values from class homework 3-1
        """
        a1 = 4.0
        a2 = 12.0
        test = cross_section(a1, a2)
        real = 0.925
        self.assertAlmostEqual(test, real, places=3)

        a3 = 1.0
        a4 = 4.0
        test = cross_section(a3, a4)
        real = 0.412
        self.assertAlmostEqual(test, real, places=3)

import unittest
from stoppingpower.cmsp import *
from stoppingpower.materials import materials
from stoppingpower.range import rangeout, exit_energy, range_equation, energy_deposition
import logging


logging.basicConfig(filename='example.log',level=logging.DEBUG)

class TestCollisionalMassStoppingPower(unittest.TestCase):
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

    def test_sc_500_mev_per_nucleon_si_in_al_sc(self):
        logging.info("1a. S_c: 500 MeV/nucleon Si in Al")
        self.almost(423.0, S_c(14.0, materials.get("Aluminum, 13"), 500.0*28, 27.977))

    def test_25_mev_proton_in_water_sc(self):
        logging.info("1b. S_c: 25 MeV Proton in Water")
        self.almost(21.75, S_c(1.0, materials.get("Water"), 25.0, 1.0))

    def test_1200_mev_carbon_in_concrete_sc(self):
        logging.info("1c. S_c: 1200 MeV Carbon in Concrete")
        self.almost(216.8, S_c(6.0, materials.get("Concrete"), 1200.0, 12.0))

    def test_10_mev_alpha_in_air_sc(self):
        logging.info("1d. S_c: 10.0 MeV alpha in Air")
        self.almost(463.7, S_c(2.0, materials.get("Air"), 10.0, 4.001506466))

    def test_330_mev_per_nucleon_fe_in_lead_sc(self):
        logging.info("1e. S_c: 330 MeV/nucleon Fe (Z=26, A=56) in Lead")
        self.almost(1147.0, S_c(26.0, materials.get("Lead, 82"), 330.0 * 56.0, 56.0))

    def test_range_45_mev_proton_in_water(self):
        logging.info("2a. Range: 45 MeV proton in water")
        self.almost(1.841, rangeout(1.0, materials.get("Water"), 45.0, 1.0))

    def test_range_600_mev_carbon_in_lead(self):
        logging.info("2b. Range: 600 MeV Carbon in Lead")
        self.almost(0.151, rangeout(6.0, materials.get("Lead, 82"), 600.0, 12.0))

    def test_range_500_mev_per_nucleon_ar_in_concrete(self):
        logging.info("2c. Range: 500 MeV/nucleon Ar (Z=18, A=40) in concrete")
        self.almost(7.46, rangeout(18.0, materials.get("Concrete"), 500.0 * 40.0, 39.948)) # He thinks 7.06

    def test_range_20_mev_proton_in_air(self):
        logging.info("2d. Range: 20 MeV proton in air")
        self.almost(403.0, rangeout(1.0, materials.get("Air"), 20.0, 1.0))

    def test_range_200_mev_per_nucleon_ne_in_al(self):
        logging.info("2e. Range: 200 MeV/nucleon Ne (Z=10, A=20) in Aluminum")
        self.almost(2.493, rangeout(10.0, materials.get("Aluminum, 13"), 200.0 * 20.0, 20.0))

    def test_exit_energy_600_mev_per_nucleon_oxygen_through_1_cm_al(self):
        logging.info("3.a.ii Exit Energy: 600 MeV/nucleon Oxygen (Z=8, A=16) through 1cm Aluminum = 578 MeV/nucleon")
        self.almost(578*16.0, exit_energy(8.0, materials.get("Aluminum, 13"), 600*16.0, 16.0, .01 * 100))

    def test_exit_energy_500_mev_proton_through_8_mm_pb(self):
        logging.info("3.b.ii Exit Energy: 500 MeV proton through 8mm of lead = 487 MeV")
        self.almost(487.0, exit_energy(1.0, materials.get("Lead, 82"), 500.0, 1.0, .008 * 100))

    def test_exit_energy_430_mev_per_nucleon_n_through_2_cm_concrete(self):
        logging.info("3.c.ii Exit Energy: 430 MeV/nucleon Nitrogen (Z=7, A=14) through 2cm of concrete= 419.4 MeV/nucleon")
        self.almost(389.0*14.0, exit_energy(7.0, materials.get("Concrete"), 430*14.0, 14.0, .02 * 100))

    def test_exit_energy_260_mev_per_nucleon_alpha_through_4_cm_water(self):
        logging.info("3.d.ii Exit Energy: 260 MeV/nucleon alpha through 4 cm water = 244.4 MeV/nucleon")
        self.almost(244.4*4, exit_energy(2.0, materials.get("Water"), 260*4.0, 4.0, .04 * 100))

    def test_exit_energy_800_mev_proton_through_1_km_air(self):
        logging.info("3.e.ii Exit Energy: 800 MeV proton through 1km air = 536 MeV")
        self.almost(536.0, exit_energy(1.0, materials.get("Air"), 800.0, 1.0, 1000.0 * 100))

    def test_energy_deposited_600_mev_per_nucleon_oxygen_through_1_cm_al(self):
        logging.info("3.a.i Energy deposited: 600 MeV/nucleon Oxygen (Z=8, A=16) through 1cm Aluminum")
        self.almost(354.0, energy_deposition(8.0, materials.get("Aluminum, 13"), 600.0 * 16, 16.0, .01 * 100))

    def test_energy_deposited_500_mev_proton_through_8_mm_pb(self):
        logging.info("3.b.i Energy deposited: 500 MeV proton through 8mm of lead")
        self.almost(13.0, energy_deposition(1.0, materials.get("Lead, 82"), 500.0, 1.0, .008 * 100))

    def test_energy_deposited_430_mev_per_nucleon_nitrogen_through_2_cm_concrete(self):
        logging.info("3.c.i Energy deposited: 430 MeV/nucleon Nitrogen (Z=7, A=14) through 2cm concrete")
        self.almost(570.0, energy_deposition(7.0, materials.get("Concrete"), 430.0 * 14, 14.0, .02 * 100))

    def test_energy_deposited_260_mev_per_nucleon_alpha_through_4_cm_water(self):
        logging.info("3.d.i Energy deposited: 260 MeV/nucleon alpha through 4 cm water")
        self.almost(62.4, energy_deposition(2.0, materials.get("Water"), 260.0 * 4, 4.001506466, .04 * 100))

    def test_energy_deposited_800_mev_proton_through_1_km_air(self):
        logging.info("3.e.i Energy deposited: 800 MeV proton through 1km air")
        self.almost(264.0, energy_deposition(1.0, materials.get("Air"), 800.0, 1.0, 1000.0 * 100))


if __name__ == "__main__":
    unittest.main()

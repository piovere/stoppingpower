from selenium import webdriver
import unittest


class CMSPTest(unittest.TestCase):

    def setUp(self):
        browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def test_can_calculate_collisional_mass_stopping_power(self):
        # J.R. opens the browser and sees a page to calculate stopping power
        browser.get('http://localhost:8000/stoppingpower/')

        # The title of the page is "Stopping Power"


        # There is a pulldown to select the shielding material

        # There is a box to enter the incident Z

        # If they type in something besides an integer, an alert box says no, and the text box is cleared

        # There is a box to enter the incident T. The units next to the box say "MeV"

        # If they type in something besides an integer, an alert box says no and the text box is cleared

        # If the number entered is less than 1 MeV, an alert box says no and the text box is cleared

        # There is a submit button

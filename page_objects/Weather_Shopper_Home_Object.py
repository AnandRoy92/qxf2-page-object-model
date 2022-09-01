"""
This class models the main Selenium tutorial page.
This form consists of some buttons
"""
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Weather_Shopper_Home_Object:
    "Page Object for the form"

    #locators
    moisturizers_button = locators.moisturizers_button

    @Wrapit._exceptionHandler
    @Wrapit._screenshot

    def buy_moisturizers(self):
        "Click on moisturizers button"
        moisturizer_button = self.click_element(self.moisturizers_button)
        return moisturizer_button
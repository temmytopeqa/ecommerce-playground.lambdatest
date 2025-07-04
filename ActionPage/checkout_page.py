from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LocatorPage.locator_home import CheckoutPageLocators  # Make sure this locator class exists

from ActionPage.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_guest_checkout_form(self, firstname, lastname, email, phone, address, city, postcode, country, region):
        # existing form code...
        pass

    def uncheck_newsletter_if_checked(self):
        newsletter_checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CheckoutPageLocators.NEWSLETTER_CHECKBOX)
        )
        if newsletter_checkbox.is_selected():
            newsletter_checkbox.click()

    def agree_and_continue(self):
        pass

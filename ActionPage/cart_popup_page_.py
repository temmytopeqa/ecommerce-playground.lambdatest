from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ActionPage.base_page import BasePage
from LocatorPage.locator_home import CartPopupPageLocators

class CartPopupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def click_proceed_to_checkout(self):
        button = self.wait.until(
            EC.element_to_be_clickable(CartPopupPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        )
        button.click()





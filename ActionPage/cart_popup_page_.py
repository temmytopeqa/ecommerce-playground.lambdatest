from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ActionPage.base_page import BasePage
from LocatorPage.locator_home import CartPopupPageLocators  # adjust if using cart_popup_locators.py

class CartPopupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def click_view_cart(self):
        self.click(CartPopupPageLocators.VIEW_CART_BUTTON)

    def click_checkout(self):
        self.click(CartPopupPageLocators.CHECKOUT_BUTTON)

    def click_proceed_to_checkout(self):
        button = self.wait.until(
            EC.element_to_be_clickable(CartPopupPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        )
        button.click()

    def click_proceed_to_checkout(self):
        pass





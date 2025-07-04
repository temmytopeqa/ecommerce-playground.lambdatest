from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ActionPage.base_page import BasePage
from LocatorPage.locator_home import ProductPageLocators

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sort_by_price_low_to_high(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.SORT_DROPDOWN)
        )
        Select(dropdown).select_by_visible_text("Price (Low > High)")

    def hover_and_add_to_cart(self):
        wait = WebDriverWait(self.driver, 10)

        # Wait for the first product to load
        product = wait.until(
            EC.presence_of_element_located(ProductPageLocators.FIRST_PRODUCT)
        )

        # Scroll into view just in case
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product)

        # Hover to reveal hidden buttons
        actions = ActionChains(self.driver)
        actions.move_to_element(product).pause(1).perform()

        # Ensure the Add to Cart button is present and clickable
        add_to_cart_btn = wait.until(
            EC.element_to_be_clickable(ProductPageLocators.FIRST_PRODUCT_ADD_TO_CART)
        )

        add_to_cart_btn.click()
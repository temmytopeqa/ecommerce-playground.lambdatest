from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from LocatorPage.locator_home import ProductPageLocators
from ActionPage.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def hover_and_add_to_cart(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            print("🟡 Locating first product...")
            product = wait.until(EC.presence_of_element_located(ProductPageLocators.FIRST_PRODUCT))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product)

            print("🟡 Hovering over product...")
            actions = ActionChains(self.driver)
            actions.move_to_element(product).pause(2).perform()

            print("🟡 Waiting for Add to Cart button...")
            add_to_cart_btn = wait.until(
                EC.element_to_be_clickable(ProductPageLocators.FIRST_PRODUCT_ADD_TO_CART)
            )

            print("🟢 Clicking Add to Cart...")
            try:
                add_to_cart_btn.click()
            except:
                self.driver.execute_script("arguments[0].click();", add_to_cart_btn)

        except TimeoutException:
            self.driver.save_screenshot("error_add_to_cart.png")
            raise Exception("❌ Failed to find or click the Add to Cart button on the first product.")

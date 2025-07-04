from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text):
        self.driver.find_element(locator).clear()
        self.driver.find_element(locator).send_keys(text)

    def click(self, locator):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def hover_and_click(self, menu_locator, submenu_locator, timeout=40):
        menu = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(menu_locator)
        )
        submenu = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(submenu_locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(menu).move_to_element(submenu).click().perform()

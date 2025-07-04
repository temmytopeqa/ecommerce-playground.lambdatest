# ActionPage/home_page.py
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ActionPage.base_page import BasePage
from LocatorPage.locator_home import HomePageLocators
from LocatorPage.locator_home import MenuLocators  # Make sure this exists

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_homepage(self):
        self.driver.get("https://ecommerce-playground.lambdatest.io/")

    def click_shop_by_category(self):
        self.click(HomePageLocators.SHOP_BY_CATEGORY)

    def navigate_to_headphones_from_mega_menu(self):
        print("Navigating to Headphones via Mega Menu...")

        # Hover on "Mega Menu"
        mega_menu = self.wait.until(EC.visibility_of_element_located(HomePageLocators.MEGA_MENU))
        actions = ActionChains(self.driver)
        actions.move_to_element(mega_menu).perform()

        time.sleep(1)  # Wait for submenu to appear

        # Click "Headphones" under MP3 Players
        headphones = self.wait.until(EC.element_to_be_clickable(MenuLocators.HEADPHONES_LINK))
        headphones.click()

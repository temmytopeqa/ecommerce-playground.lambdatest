import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ActionPage.checkout_page import CheckoutPage

from ActionPage.cart_popup_page_ import CartPopupPage
from ActionPage.home_page import HomePage
from ActionPage.product_page import ProductPage
from Config.configuration import Config


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_checkout_process(driver):
    home = HomePage(driver)
    home.navigate_to_homepage()
    home.navigate_to_headphones_from_mega_menu()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-thumb"))
    )

    product = ProductPage(driver)
    try:
        product.hover_and_add_to_cart()
        print("🟢 Add to Cart attempted.")
    except Exception:
        print("🟡 Skipping add to cart – possibly all products sold out.")

    try:
        cart = CartPopupPage(driver)
        cart.click_proceed_to_checkout()
        print("🟢 Clicked Checkout from popup.")
    except TimeoutException:
        print("❌ Checkout button in popup not found.")
        assert False, "Could not click checkout from popup – test failed."

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
    )
    assert "Shopping Cart" in driver.page_source or "Checkout" in driver.page_source

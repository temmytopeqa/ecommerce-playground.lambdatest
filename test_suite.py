import pytest
from selenium import webdriver
from ActionPage.home_page import HomePage
from ActionPage.product_page import ProductPage
from ActionPage.cart_popup_page_ import CartPopupPage
from ActionPage.checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://ecommerce-playground.lambdatest.io/")
    yield driver
    driver.quit()

def test_checkout_process(driver):
    # Step 1: Navigate to homepage and go to headphones
    home = HomePage(driver)
    home.navigate_to_homepage()
    home.navigate_to_headphones_from_mega_menu()

    # Step 2: Wait for product list to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-thumb"))
    )

    # Step 3: Add first product to cart
    product = ProductPage(driver)
    product.hover_and_add_to_cart()

    # Step 4: Proceed to checkout from cart popup
    cart = CartPopupPage(driver)
    cart.click_proceed_to_checkout()

    # Step 5: Fill guest checkout form
    checkout = CheckoutPage(driver)
    checkout.fill_guest_checkout_form(
        firstname="Temmy",
        lastname="Tope",
        email="temmy@example.com",
        phone="1234567890",
        address="12 Test Street",
        city="Lagos",
        postcode="100001",
        country="Nigeria",
        region="Lagos"
    )
    checkout.uncheck_newsletter_if_checked()
    checkout.agree_and_continue()

    # ✅ Step 6: Assert successful order
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#content h1"))
    )
    assert "Success" in driver.page_source or "Your order has been placed" in driver.page_source

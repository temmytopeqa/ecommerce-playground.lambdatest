from selenium.webdriver.common.by import By

class BasePageLocators:
    pass

class HomePageLocators:
    # SHOP_BY_CATEGORY = None
    MEGA_MENU = (By.LINK_TEXT, "Mega Menu")
    MP3_PLAYERS = (By.LINK_TEXT, "MP3 Players")

class MenuLocators:
    HEADPHONES_LINK = (By.LINK_TEXT, "Headphones")  # or correct locator under Mega Menu

class ProductPageLocators:
    FIRST_PRODUCT = (
        By.XPATH,
        "(//div[contains(@class, 'product-thumb')])[1]"
    )
    FIRST_PRODUCT_ADD_TO_CART = (
        By.XPATH,
        "(//div[contains(@class, 'product-thumb')])[1]//button[contains(@aria-label, 'Add to Cart')]"
    )
    SORT_DROPDOWN = (By.ID, "input-sort-212403")

# class ProductPageLocators:
#     FIRST_PRODUCT = (By.XPATH, "(//div[@class='product-thumb'])[1]")
#     FIRST_PRODUCT_ADD_TO_CART = (By.XPATH, "(//div[@class='product-thumb'])[1]//button[@aria-label='Add to Cart']")
#     SORT_DROPDOWN = (By.ID, "input-sort-212403")
#     PRODUCT_THUMBNAIL = (By.XPATH, "(//div[@class=\'product-thumb\'])[1]")
#     ADD_TO_CART_BUTTON = (By.XPATH, "(//div[@class=\'product-thumb\'])[1]//button[@aria-label=\'Add to Cart\']")

class CartPopupPageLocators:
    VIEW_CART_BUTTON = (By.XPATH, "//a[normalize-space()=\'View Cart\']")
    CHECKOUT_BUTTON = (By.XPATH, "//a[normalize-space()=\'Checkout\']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn-primary[href*='checkout']")

class CheckoutPageLocators:
    # PRODUCTS ARE OUT OF STOCK
    # PAYMENT_CONTINUE_BUTTON = BLOCKER I COULD NOT CONTINUE WITH PAYMENT
    # FIRST_NAME_FIELD = (By.ID, "input-payment-firstname")
    # LAST_NAME_FIELD = (By.ID, "input-payment-lastname")
    # EMAIL_FIELD = (By.ID, "input-payment-email")
    # TELEPHONE_FIELD = (By.ID, "input-payment-telephone")
    # ADDRESS_1_FIELD = (By.ID, "input-payment-address-1")
    # CITY_FIELD = (By.ID, "input-payment-city")
    # POSTCODE_FIELD = (By.ID, "input-payment-postcode")
    # COUNTRY_DROPDOWN = (By.ID, "input-payment-country")
    # REGION_DROPDOWN = (By.ID, "input-payment-zone")
    # SHIPPING_CONTINUE_BUTTON = (By.ID, "button-shipping-method")
    # PAYMENT_METHOD_CHECKBOX = (By.XPATH, "//input[@name=\'payment_method\']")
    # TERMS_AND_CONDITIONS_CHECKBOX = (By.NAME, "agree")
    # CONFIRM_ORDER_BUTTON = (By.ID, "button-confirm")

    class CheckoutLocators:
        # Add this to existing class
        NEWSLETTER_CHECKBOX = (By.NAME, "newsletter")
 # NEWSLETTER CHECK BOX
 # NEWSLETTER_CHECKBOX = (By.XPATH, "//input[@name='newsletter' and @type='checkbox']")



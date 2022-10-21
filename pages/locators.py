from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,'.btn-add-to-basket')
    BOOK_NAME_MESSAGES = (By.CSS_SELECTOR, 'div.alertinner strong')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner p strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
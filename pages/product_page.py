from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_book_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    def check_book_name(self):
        success_messages = self.browser.find_elements(*ProductPageLocators.BOOK_NAME_MESSAGES)
        book_name_message = success_messages[0].text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == book_name_message, 'Added book name is wrong'

    def check_book_price(self):
        success_messages = self.browser.find_elements(*ProductPageLocators.BOOK_NAME_MESSAGES)
        book_price_message = success_messages[2].text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book_price == book_price_message, f'Added book price is wrong! ' \
                                                 f'Book price message is {book_price_message} and' \
                                                 f'book price is {book_price}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_NAME_MESSAGES), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_NAME_MESSAGES), \
            'Success message must be disappeared, but it is not'

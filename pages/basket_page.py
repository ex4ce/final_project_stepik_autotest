from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty but should be'

    def is_empty_basket_message_presented(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
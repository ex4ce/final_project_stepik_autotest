from .pages.product_page import ProductPage
import time
import pytest

#link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_book_to_cart()
    page.solve_quiz_and_get_code()
    #time.sleep(2)
    page.check_book_name()
    page.check_book_price()

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6",
                                        pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket_promo(browser,promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_cart()
    page.solve_quiz_and_get_code()
    # time.sleep(2)
    page.check_book_name()
    page.check_book_price()
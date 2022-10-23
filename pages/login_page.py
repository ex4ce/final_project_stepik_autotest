from .base_page import BasePage
from .locators import LoginPageLocators
import faker

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'Login substring is not in URL'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        #fake_email = faker.Faker().email()
        #fake_pass = '123fsdfj1233'
        mail = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        passw = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        conf_passw = self.browser.find_element(*LoginPageLocators.REGISTER_CONF_PASS)
        send_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        mail.send_keys(email)
        passw.send_keys(password)
        conf_passw.send_keys(password)
        send_button.click()

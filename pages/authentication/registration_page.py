from playwright.sync_api import Page, expect
import re
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, "registration-page-registration-button", "Registration")
        self.login_link = Link(page, "registration-page-login-link", "Login")

    def click_registration_button(self):
        self.registration_button.check_enabled()
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(r".*/#/auth/login"))

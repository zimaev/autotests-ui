from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, "registration-page-registration-button", "Registration")

    def click_registration_button(self):
        self.registration_button.check_enabled()
        self.registration_button.click()

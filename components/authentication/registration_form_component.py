import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.Input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = Input(page, "registration-form-email-input", "Email")
        self.username_input = Input(page, "registration-form-username-input", "Username")
        self.password_input = Input(page, "registration-form-password-input", "Password")

    @allure.step("Проверяю видимость формы регистрации")
    def check_visible(self, email: str, username: str, password: str):
        self.email_input.check_have_value(email)
        self.username_input.check_have_value(username)
        self.password_input.check_have_value(password)

    @allure.step("Заполняю форму регистрации")
    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.check_visible(email=email, username=username, password=password)

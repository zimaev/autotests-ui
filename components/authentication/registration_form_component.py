from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        self.username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        self.password_input = page.get_by_test_id("registration-form-password-input").locator("input")

    def check_visible(self, email: str, username: str, password: str):
        expect(self.email_input, "email введён некорректно").to_have_value(email)
        expect(self.username_input, "username введён некорректно").to_have_value(username)
        expect(self.password_input, "password введён некорректно").to_have_value(password)

    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.check_visible(email=email, username=username, password=password)

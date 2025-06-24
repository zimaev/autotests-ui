from playwright.sync_api import expect, sync_playwright, Page
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    # Открыть страницу
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Локаторы страницы регистрации
    email_input = chromium_page.get_by_test_id("registration-form-email-input").locator("input")
    username_input = chromium_page.get_by_test_id("registration-form-username-input").locator("input")
    password_input = chromium_page.get_by_test_id("registration-form-password-input").locator("input")
    registration_button = chromium_page.get_by_test_id("registration-page-registration-button")

    # Заполнение полей Email, Username, Password
    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")

    # Нажмет на кнопку "Registration"
    registration_button.click()

    # Локаторы страница Dashboard
    dashboard_toolbar_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")

    # Проверки, что на странице "Dashboard" отображается заголовок "Dashboard"
    expect(chromium_page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    expect(dashboard_toolbar_title).to_be_visible()
    expect(dashboard_toolbar_title).to_have_text("Dashboard")


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password",
                         [("user.name@gmail.com", "password"),
                          ("user.name@gmail.com", "  "),
                          ("  ", "password")], )
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    login_button = chromium_page.get_by_test_id('login-page-login-button')
    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')

    email_input.fill(email)
    password_input.fill(password)
    login_button.click()

    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

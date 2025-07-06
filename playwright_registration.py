from playwright.sync_api import sync_playwright, expect

from config import settings

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()
    # Открыть страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Локаторы страницы регистрации
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    registration_button = page.get_by_test_id("registration-page-registration-button")

    # Заполнение полей Email, Username, Password
    email_input.fill(settings.test_user.email)
    username_input.fill(settings.test_user.username)
    password_input.fill(settings.test_user.password)

    # Нажмет на кнопку "Registration"
    registration_button.click()

    # Локаторы страница Dashboard
    dashboard_toolbar_title = page.get_by_test_id("dashboard-toolbar-title-text")

    # Проверки, что на странице "Dashboard" отображается заголовок "Dashboard"
    expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    expect(dashboard_toolbar_title).to_be_visible()
    expect(dashboard_toolbar_title).to_have_text("Dashboard")

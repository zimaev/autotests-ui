from playwright.sync_api import sync_playwright, expect, Page, Playwright
import pytest


@pytest.fixture(scope="session")
def initialize_browser_state():
    """
     - регистрирует нового пользователя
     - сохранять состояние браузера
     - выполняться один раз за всю сессию тестирования.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Открыть страницу
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Локаторы страницы регистрации
        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        registration_button = page.get_by_test_id("registration-page-registration-button")

        # Заполнение полей Email, Username, Password
        email_input.fill("user.name@gmail.com")
        username_input.fill("username")
        password_input.fill("password")

        # Нажмет на кнопку "Registration"
        registration_button.click()

        # Сохранить состояние браузера
        dashboard_toolbar_title = page.get_by_test_id("dashboard-toolbar-title-text")
        expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        expect(dashboard_toolbar_title).to_be_visible()
        expect(dashboard_toolbar_title).to_have_text("Dashboard")
        context.storage_state(path="browser-state.json")


@pytest.fixture(autouse=True)
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    """
    - открывает новую страницу браузера, используя сохраненное состояние browser-state.json.
    - запускается на каждый автотест.
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()
    yield page
    page.close()

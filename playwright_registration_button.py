from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    # Открыть страницу регистрации: https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration.
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Локаторы страницы регистрации
    registration_button = page.get_by_test_id("registration-page-registration-button")

    # Проверить, что кнопка "Registration" находится в состоянии disabled.
    expect(registration_button).to_be_disabled()

    # Заполнение полей Email, Username, Password
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")

    # Проверить, что кнопка "Registration" перешла в состояние enabled.
    expect(registration_button).to_be_enabled()

from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
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

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        # Открыть страницу /courses
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Локаторы страницы курсов
        courses_toolbar_title = page.get_by_test_id("courses-list-toolbar-title-text")
        empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
        list_empty_view_title = page.get_by_test_id("courses-list-empty-view-title-text")
        empty_view_description = page.get_by_test_id("courses-list-empty-view-description-text")

        # Проверки
        # Проверяем что открыт url без регистрации
        expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Заголовок
        expect(courses_toolbar_title).to_be_visible()
        expect(courses_toolbar_title).to_have_text("Courses")

        # Иконка
        expect(empty_view_icon).to_be_visible()

        # Текст There is no results
        expect(list_empty_view_title).to_be_visible()
        expect(list_empty_view_title).to_have_text("There is no results")

        # Текст Results from the load test pipeline will be displayed here
        expect(empty_view_description).to_be_visible()
        expect(empty_view_description).to_have_text("Results from the load test pipeline will be displayed here")
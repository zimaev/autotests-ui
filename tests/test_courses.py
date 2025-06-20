from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        
        # Локаторы страницы курсов
        courses_toolbar_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
        empty_view_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
        list_empty_view_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
        empty_view_description = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")

        # Проверки
        # Проверяем что открыт url без регистрации
        expect(chromium_page_with_state).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

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
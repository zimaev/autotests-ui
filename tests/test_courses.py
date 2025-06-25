import pytest
from playwright.sync_api import expect, Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    empty_view_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    empty_view_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')

    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')
    expect(empty_view_icon).to_be_visible()
    expect(empty_view_title).to_be_visible()
    expect(empty_view_title).to_have_text('There is no results')
    expect(empty_view_description).to_be_visible()
    expect(empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')


@pytest.mark.courses
@pytest.mark.regression
def test_create_courses(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    # Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create.
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # Проверить наличие заголовка "Create course" с помощью метода check_visible_create_course_title.
    create_course_page.check_visible_create_course_title()

    # Проверить, что кнопка создания курса недоступна для нажатия — метод check_disabled_create_course_button.
    create_course_page.check_disabled_create_course_button()

    # Убедиться, что отображается пустой блок для предпросмотра изображения — метод check_visible_image_preview_empty_view.
    create_course_page.check_visible_image_preview_empty_view()

    # Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана — метод check_visible_image_upload_view.
    create_course_page.check_visible_image_upload_view()

    # Проверить, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.check_visible_create_course_form(title="",
                                                        description="",
                                                        estimated_time="",
                                                        max_score="0",
                                                        min_score="0")
    # Проверить наличие заголовка "Exercises"
    create_course_page.check_visible_exercises_title()

    # Проверить наличие кнопки создания задания
    create_course_page.check_visible_create_exercise_button()

    # Убедиться, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # Загрузить изображение для превью курс
    create_course_page.upload_preview_image("../testdata/files/image.png")

    # Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.check_visible_image_upload_view()

    # Заполнить форму создания курса
    create_course_page.fill_create_course_form(title="Playwright",
                                               estimated_time="2 weeks",
                                               description="Playwright",
                                               max_score="100",
                                               min_score="10")
    # Нажать на кнопку создания курса
    create_course_page.click_create_course_button()

    # наличие заголовка "Courses"
    courses_list_page.check_visible_courses_title()

    # наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()

    # корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(index=0,
                                                title="Playwright",
                                                max_score="100",
                                                min_score="10",
                                                estimated_time="2 weeks")

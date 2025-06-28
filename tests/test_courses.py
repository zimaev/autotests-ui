import pytest
from pathlib import Path

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    """
    Отображение компонента Navbar - проверяет, что компонент Navbar корректно отображается на странице
    Отображение компонента Sidebar - проверяет, что компонент Sidebar виден и корректно отрисован
    Отображение заголовка "Courses" - проверяет наличие и корректное отображение заголовка страницы
    Отображение кнопки создания курса - проверяет, что кнопка для создания нового курса отображается
    Отображение пустого блока с текстом "There is no results"- при отсутствии курсов отображается соответствующий блок
    """
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_courses(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    # Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create.
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    #  Проверить наличие заголовка "Create course"  Проверить, что кнопка создания курса недоступна для нажатия
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)

    # Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана — метод check_visible_image_upload_view.
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

    # Проверить, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.create_course_form.check_visible(title="",
                                                        description="",
                                                        estimated_time="",
                                                        max_score="0",
                                                        min_score="0")
    # Проверить наличие заголовка "Exercises" и кнопки создания задания
    create_course_page.create_exercises_toolbar.check_visible()

    # Убедиться, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # Загрузить изображение для превью курс
    image_path = Path(__file__).parents[1] / "testdata" / "files" / "image.png"
    create_course_page.image_upload_widget.upload_preview_image(image_path)

    # Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    # Заполнить форму создания курса
    create_course_page.create_course_form.fill(title="Playwright",
                                               estimated_time="2 weeks",
                                               description="Playwright",
                                               max_score="100",
                                               min_score="10")

    # Проверить, что кнопка создания курса доступна для нажатия.
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)

    # Нажать на кнопку создания курса
    create_course_page.create_course_toolbar.click_create_course_button()

    # наличие заголовка "Courses"
    courses_list_page.toolbar_view.check_visible()

    # корректность отображаемых данных на карточке курса
    courses_list_page.course_view.check_visible(index=0,
                                                title="Playwright",
                                                max_score="100",
                                                min_score="10",
                                                estimated_time="2 weeks")

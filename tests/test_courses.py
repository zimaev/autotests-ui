import pytest
from playwright.sync_api import expect, Page


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


@pytest.mark.parametrize(
    "input_value",
    [
        pytest.param(1, marks=pytest.mark.xfail(reason="Known issue with 1")),
        2,
        pytest.param(3, marks=pytest.mark.skip(reason="Feature not implemented for 3")),
    ]
)
def test_function(input_value):
    assert input_value != 1
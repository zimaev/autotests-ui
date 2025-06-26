import pytest
from playwright.sync_api import Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)


@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)


@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)


@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page_with_state)

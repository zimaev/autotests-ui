import pytest
import allure
from allure_commons.types import Severity

from config import settings
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("Проверка успешной авторизации")
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(self,
                                      registration_page: RegistrationPage,
                                      dashboard_page: DashboardPage,
                                      login_page: LoginPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(email=settings.test_user.email,
                                                 username=settings.test_user.username,
                                                 password=settings.test_user.password)
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email=settings.test_user.email,
                                   password=settings.test_user.password)
        login_page.click_login_button()
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("email, password",
                             [
                                 ("user.name@gmail.com", "password"),
                                 ("user.name@gmail.com", "  "),
                                 ("  ", "password")
                             ])
    def test_wrong_email_or_password_authorization(self,
                                                   login_page: LoginPage,
                                                   email: str,
                                                   password: str):
        allure.dynamic.title(f'Проверка авторизации с некорректными данными email={email}, password={password}')
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.severity(Severity.NORMAL)
    @allure.title("Проверка перехода из страницы авторизации, на страницу регистрации")
    def test_navigate_from_authorization_to_registration(self,
                                                         login_page: LoginPage,
                                                         registration_page: RegistrationPage):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()
        registration_page.registration_form.check_visible(email="",
                                                          username="",
                                                          password="")

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:

    @allure.severity(Severity.CRITICAL)
    @allure.title("Успешная регистрация")
    def test_successful_registration(self,
                                     registration_page: RegistrationPage,
                                     dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(email=settings.test_user.email,
                                                 username=settings.test_user.username,
                                                 password=settings.test_user.password)
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar.check_visible()

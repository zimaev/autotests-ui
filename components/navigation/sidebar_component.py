import allure
from playwright.sync_api import Page
import re
from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, prefix='logout')
        self.courses_list_item = SidebarListItemComponent(page, prefix='courses')
        self.dashboard_list_item = SidebarListItemComponent(page, prefix='dashboard')

    @allure.step("Проверяю что сайд-бар отображается")
    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    @allure.step("Кликаю в сайд-баре Logout")
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step("Кликаю в сайд-баре Courses")
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    @allure.step("Кликаю в сайд-баре Dashboard")
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))

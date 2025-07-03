from typing import Pattern
import allure

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Открытие URL-адреса {url}'):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f'Перезагрузка страницы "{self.page.url}"'):
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Проверка соответствия текущего URL-адреса шаблону "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)

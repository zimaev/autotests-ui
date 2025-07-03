import allure
from playwright.sync_api import Page, Locator, expect


class BaseElement:

    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        return "type_of"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        with allure.step(f'Получение локатора "data-testid={locator}" с индексом "{nth}"'):
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        with allure.step(f'Клик {self.type_of} "{self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        with allure.step(f'Проверяем что {self.type_of} "{self.name}" отображается'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f'Проверяем что {self.type_of} "{self.name}" имеет текст {text}'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)

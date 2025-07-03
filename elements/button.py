import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):

    @property
    def type_of(self) -> str:
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Проверяю, что {self.type_of} "{self.name}" активен'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()

    def check_disabled(self, **kwargs):
        with allure.step(f'Проверяю, что {self.type_of} "{self.name}" не активен'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_disabled()

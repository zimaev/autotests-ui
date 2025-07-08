import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("BUTTON")


class Button(BaseElement):

    @property
    def type_of(self) -> str:
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        step = f'Проверяю, что {self.type_of} "{self.name}" активен'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

    def check_disabled(self, **kwargs):
        step = f'Проверяю, что {self.type_of} "{self.name}" не активен'
        with allure.step(f'Проверяю, что {self.type_of} "{self.name}" не активен'):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()

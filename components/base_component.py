from typing import Pattern

from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger("BASE_COMPONENT")


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        logger.info(f"Проверка текущего url {expected_url}")
        expect(self.page).to_have_url(expected_url)

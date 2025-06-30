from typing import Pattern

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, prefix: str):
        super().__init__(page)

        self.icon = Icon(page, f'{prefix}-drawer-list-item-icon', "Icon")
        self.title = Text(page, f'{prefix}-drawer-list-item-title-text', "Title")
        self.button = Button(page, f'{prefix}-drawer-list-item-button', "Button")

    def check_visible(self, title: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)

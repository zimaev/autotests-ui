import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, prefix: str):
        super().__init__(page)
        self.icon = Icon(page, f'{prefix}-empty-view-icon', "Icon")
        self.title = Text(page, f'{prefix}-empty-view-title-text', "Title")
        self.description = Text(page, f'{prefix}-empty-view-description-text', "Description")

    @allure.step("Проверяю видимость пустого {title}")
    def check_visible(self, title: str, description: str):
        # Проверяем видимость иконки
        self.icon.check_visible()

        # Проверяем видимость заголовка и его текст
        self.title.check_visible()

        self.title.check_have_text(title)

        # Проверяем видимость описания и его текст
        self.description.check_visible()
        self.description.check_have_text(description)

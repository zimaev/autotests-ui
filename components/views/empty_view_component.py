from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, prefix: str):
        super().__init__(page)
        self.icon = page.get_by_test_id(f'{prefix}-empty-view-icon')
        self.title = page.get_by_test_id(f'{prefix}-empty-view-title-text')
        self.description = page.get_by_test_id(f'{prefix}-empty-view-description-text')

    def check_visible(self, title: str, description: str):
        # Проверяем видимость иконки
        expect(self.icon).to_be_visible()

        # Проверяем видимость заголовка и его текст
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        # Проверяем видимость описания и его текст
        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(description)

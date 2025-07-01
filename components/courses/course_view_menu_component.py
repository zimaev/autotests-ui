from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.menu_button = Button(page, 'course-view-menu-button', "Menu")
        self.edit_menu_item = Button(page, 'course-view-edit-menu-item', "Edit")
        self.delete_menu_item = Button(page, 'course-view-delete-menu-item', "Delete")

    def click_edit_course(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_item.check_visible(nth=index)
        self.edit_menu_item.click(nth=index)

    def click_delete_course(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_item.check_visible(nth=index)
        self.delete_menu_item.click(nth=index)

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, prefix: str):
        super().__init__(page)
        self.preview_empty_view = EmptyViewComponent(page, prefix)

        self.preview_image = Image(page,
                                   f'{prefix}-image-upload-widget-preview-image',
                                   "Preview Image")

        self.image_upload_info_icon = Icon(page,
                                           f'{prefix}-image-upload-widget-info-icon',
                                           "Icon")

        self.image_upload_info_title = Text(page,
                                            f'{prefix}-image-upload-widget-info-title-text',
                                            "Title")

        self.image_upload_info_description = Text(page,
                                                  f'{prefix}-image-upload-widget-info-description-text',
                                                  "Description")

        self.image_upload_button = Button(page,
                                          f'{prefix}-image-upload-widget-upload-button',
                                          "Upload")

        self.image_remove_button = Button(page,
                                          f'{prefix}-image-upload-widget-remove-button',
                                          "Remove")

        self.image_upload_input = FileInput(page,
                                            f"{prefix}-image-upload-widget-input",
                                            "Upload unput")

    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible()
        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file')
        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')
        self.image_upload_button.check_visible()

        if is_image_uploaded:
            self.image_upload_input.check_visible()
            self.image_remove_button.check_visible()
        if not is_image_uploaded:
            self.preview_empty_view.check_visible(title="No image selected",
                                                  description="Preview of selected image will be displayed here")

    def click_remove_image_button(self):
        self.image_remove_button.click()

    def check_visible_preview_image(self):
        self.preview_image.check_visible()

    def upload_preview_image(self, file):
        self.image_upload_input.set_input_files(file)

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, prefix: str):
        super().__init__(page)
        self.preview_empty_view = EmptyViewComponent(page, prefix)

        self.preview_image = page.get_by_test_id(f'{prefix}-image-upload-widget-preview-image')
        self.image_upload_info_icon = page.get_by_test_id(f'{prefix}-image-upload-widget-info-icon')
        self.image_upload_info_title = page.get_by_test_id(f'{prefix}-image-upload-widget-info-title-text')
        self.image_upload_info_description = page.get_by_test_id(f'{prefix}-image-upload-widget-info-description-text')

        self.image_upload_button = page.get_by_test_id(f'{prefix}-image-upload-widget-upload-button')
        self.image_remove_button = page.get_by_test_id(f'{prefix}-image-upload-widget-remove-button')
        self.image_upload_input = page.get_by_test_id(f"{prefix}-image-upload-widget-input")

    def check_visible(self, is_image_uploaded: bool = False):
        expect(self.image_upload_info_icon).to_be_visible()
        expect(self.image_upload_info_title).to_be_visible()
        expect(self.image_upload_info_title).to_have_text('Tap on "Upload image" button to select file')
        expect(self.image_upload_info_description).to_be_visible()
        expect(self.image_upload_info_description).to_have_text('Recommended file size 540X300')
        expect(self.image_upload_button).to_be_visible()

        if is_image_uploaded:
            expect(self.image_upload_input).to_be_visible()
            expect(self.image_remove_button).to_be_visible()
        if not is_image_uploaded:
            self.preview_empty_view.check_visible(title="No image selected",
                                                  description="Preview of selected image will be displayed here")

    def click_remove_image_button(self):
        self.image_remove_button.click()

    def check_visible_preview_image(self):
        expect(self.preview_image).to_be_visible()

    def upload_preview_image(self, file):
        self.image_upload_input.set_input_files(file)

import os
import pytesseract
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.textfield import MDTextField
from PIL import Image

class ImageToTextApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Image to Text"
        self.theme_cls.primary_palette = "BlueGray"
        self.dialog = None
        self.progressbar = None
        self.image_path = None

    def build(self):
        layout = MDBoxLayout(orientation="vertical")

        # File button
        self.file_button = MDFlatButton(text="Choose an image", on_release=self.show_file_manager)
        layout.add_widget(self.file_button)

        # Image preview
        self.image_preview = MDBoxLayout(orientation="vertical")
        layout.add_widget(self.image_preview)

        # Text field
        self.text_field = MDTextField(multiline=True, hint_text="Extracted text will be shown here")
        layout.add_widget(self.text_field)

        return layout

    def show_file_manager(self, *args):
        manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
            preview=False,
        )
        manager.show("/")

    def select_path(self, path):
        self.image_path = path
        self.update_image_preview()
        self.dialog = MDDialog(
            title="Extracting text...",
            type="custom",
            content_cls=MDGridLayout(rows=2, cols=1),
            buttons=[
                MDFlatButton(text="Cancel", on_release=self.dialog_cancel),
            ],
        )
        self.progressbar = MDProgressBar()
        self.dialog.content_cls.add_widget(self.progressbar)
        self.dialog.open()
        self.extract_text()

    def update_image_preview(self):
        self.image_preview.clear_widgets()
        if self.image_path:
            image = Image.open(self.image_path)
            image_widget = MDLabel(
                text="Image preview",
                halign="center",
                font_style="H6",
                size_hint=(None, None),
                size=(self.root.width, self.root.height / 2),
            )
            image_widget.texture = image._texture
            self.image_preview.add_widget(image_widget)

    def extract_text(self):
        if self.image_path:
            text = pytesseract.image_to_string(Image.open(self.image_path))
            self.text_field.text = text
            self.dialog.dismiss()
        else:
            self.dialog_cancel()

    def dialog_cancel(self, *args):
        if self.dialog:
            self.dialog.dismiss()

    def exit_file_manager(self, *args):
        self.dialog_cancel()

if __name__ == "__main__":
    ImageToTextApp().run()

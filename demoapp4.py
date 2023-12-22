from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.uix.video import Video
from googletrans import Translator
import pytesseract
from PIL import Image
import fitz

class ImageTranslatorScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Blue"

        # File manager button
        self.file_manager_button = MDRectangleFlatButton(
            text="Select image",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            on_release=self.show_file_manager,
        )
        self.add_widget(self.file_manager_button)

    def show_file_manager(self, instance):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
            preview=True,
        )
        self.file_manager.show("/")

    def exit_file_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        # Get image text
        image = Image.open(path)
        text = pytesseract.image_to_string(image)

        # Translate text
        translator = Translator()
        translation = translator.translate(text, dest="en")

        # Show translation in a dialog
        self.dialog = MDDialog(
            title="Translation",
            text=translation.text,
            buttons=[
                MDRectangleFlatButton(
                    text="OK", on_release=self.close_dialog
                )
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class VideoTranslatorScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Red"

        # File manager button
        self.file_manager_button = MDRectangleFlatButton(
            text="Select video",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            on_release=self.show_file_manager,
        )
        self.add_widget(self.file_manager_button)

    def show_file_manager(self, instance):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
            preview=True,
        )
        self.file_manager.show("/")

    def exit_file_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        # Show video
        video = Video(source=path, state="play")
        self.add_widget(video)

class HandwrittenTranslatorScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Green"

        # File manager button
        self.file_manager_button = MDRectangleFlatButton(
            text="Select image",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            on_release=self.show_file_manager,
        )
        self.add_widget(self.file_manager_button)

    def show_file_manager(self, instance):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
            preview=True,
        )
        self.file_manager.show("/")

    def exit_file_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        # Get image text
        image = Image.open(path)
        text = pytesseract.image_to_string(image)

        # Translate text
        translator = Translator()
        translation = translator.translate(text, dest="en")

        # Show translation in a dialog
        self.dialog = MDDialog(
            title="Translation",
            text=translation.text,
            buttons=[
                MDRectangleFlatButton(
                    text="OK", on_release=self.close_dialog
                )
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class PDFTranslatorScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Purple"

        # File manager button
        self.file_manager_button = MDRectangleFlatButton(
            text="Select PDF",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            on_release=self.show_file_manager,
        )
        self.add_widget(self.file_manager_button)

    def show_file_manager(self, instance):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
            preview=True,
        )
        self.file_manager.show("/")

    def exit_file_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        # Get PDF text
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()

        # Translate text
        translator = Translator()
        translation = translator.translate(text, dest="en")

        # Show translation in a dialog
        self.dialog = MDDialog(
            title="Translation",
            text=translation.text,
            buttons=[
                MDRectangleFlatButton(
                    text="OK", on_release=self.close_dialog
                )
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class ImageTranslatorApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()
        self.image_translator_screen = ImageTranslatorScreen(name="image_translator_screen")
        self.video_translator_screen = VideoTranslatorScreen(name="video_translator_screen")
        self.handwritten_translator_screen = HandwrittenTranslatorScreen(name="handwritten_translator_screen")
        self.pdf_translator_screen = PDFTranslatorScreen(name="pdf_translator_screen")
        self.screen_manager.add_widget(self.image_translator_screen)
        self.screen_manager.add_widget(self.video_translator_screen)
        self.screen_manager.add_widget(self.handwritten_translator_screen)
        self.screen_manager.add_widget(self.pdf_translator_screen)
        return self.screen_manager

ImageTranslatorApp().run()
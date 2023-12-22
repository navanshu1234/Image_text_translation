from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivymd.app import MDApp
from kivy.lang.builder import Builder as New
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty
from kivy.core.window import Window

from pdf_translator import PDFTranslator
from image_translator import ImageTranslator
from handwriting_translator import HandwritingTranslator
from video_translator import VideoTranslator

Window.size = (300, 500)

class HomeScreen(Screen):
    pass

class ImageTranslatorScreen(Screen):
    file_manager = ObjectProperty(None)

    def show_file_manager(self):
        self.file_manager.show()

class VideoTranslatorScreen(Screen):
    file_manager = ObjectProperty(None)

    def show_file_manager(self):
        self.file_manager.show()

class HandwrittenTranslatorScreen(Screen):
    file_manager = ObjectProperty(None)

    def show_file_manager(self):
        self.file_manager.show()

class PDFTranslatorScreen(Screen):
    file_manager = ObjectProperty(None)

    def show_file_manager(self):
        self.file_manager.show()

class ImageTranslatorApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(HomeScreen(name="home_screen"))
        self.screen_manager.add_widget(ImageTranslatorScreen(name="image_translator_screen"))
        self.screen_manager.add_widget(VideoTranslatorScreen(name="video_translator_screen"))
        self.screen_manager.add_widget(HandwrittenTranslatorScreen(name="handwritten_translator_screen"))
        self.screen_manager.add_widget(PDFTranslatorScreen(name="pdf_translator_screen"))
        return self.screen_manager

    def on_start(self):
        New.load_file("image_translator.kv")
        New.load_file("video_translator.kv")
        New.load_file("handwritten_translator.kv")
        New.load_file("pdf_translator.kv")
        self.image_translator_screen = self.screen_manager.get_screen("image_translator_screen")
        self.image_translator_screen.file_manager = self.file_manager_open_image

        self.video_translator_screen = self.screen_manager.get_screen("video_translator_screen")
        self.video_translator_screen.file_manager = self.file_manager_open_video

        self.handwritten_translator_screen = self.screen_manager.get_screen("handwritten_translator_screen")
        self.handwritten_translator_screen.file_manager = self.file_manager_open_handwritten

        self.pdf_translator_screen = self.screen_manager.get_screen("pdf_translator_screen")
        self.pdf_translator_screen.file_manager = self.file_manager_open_pdf

    def file_manager_open_image(self, selection):
        self.image_translator = ImageTranslator(selection[0])
        self.image_translator.translate()
        self.show_translation(self.image_translator.result)

    def file_manager_open_video(self, selection):
        self.video_translator = VideoTranslator(selection[0])
        self.video_translator.translate()
        self.show_translation(self.video_translator.result)

    def file_manager_open_handwritten(self, selection):
        self.handwritten_translator = HandwritingTranslator(selection[0])
        self.handwritten_translator.translate()
        self.show_translation(self.handwritten_translator.result)

    def file_manager_open_pdf(self, selection):
        self.pdf_translator = PDFTranslator(selection[0])
        self.pdf_translator.translate()
        self.show_translation(self.pdf_translator.result)

    def show_translation(self, translation):
        self.dialog = MDDialog(
            title="Translation",
            text=translation,
            buttons=[
                MDFlatButton(
                    text="OK", on_release=self.close_dialog
                )
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

if __name__ == "__main__":
    ImageTranslatorApp().run()
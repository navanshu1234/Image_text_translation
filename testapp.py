from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from googletrans import Translator
from PIL import Image
import pytesseract
import cv2


#ScreenManager:
#    ImageTranslatorScreen:
 #       name: 'image_translator_screen'
  #  VideoTranslatorScreen:
   #     name: 'video_translator_screen'
    #HandwrittenTranslatorScreen:
     #   name: 'handwritten_translator_screen'
    #PdfTranslatorScreen:
     #   name: 'pdf_translator_screen'
Builder.load_string(
    """


<Tab>
    MDLabel:
        text: root.tab_title
        halign: "center"
        font_style: "H5"


<ImageTranslatorScreen>:
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Image Text Translator"
            md_bg_color: app.theme_cls.primary_color
            elevation: 10
        MDTextField:
            id: image_path
            hint_text: "Enter image path or browse"
            size_hint: None, None
            width: 400
            height: 40
            pos_hint: {"center_x": .5, "center_y": .8}
        MDRectangleFlatButton:
            text: "Browse"
            pos_hint: {"center_x": .5, "center_y": .7}
            on_release: app.browse_image()
        MDRectangleFlatButton:
            text: "Translate"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_release: app.translate_image()

<VideoTranslatorScreen>:
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Video Text Translator"
            md_bg_color: app.theme_cls.primary_color
            elevation: 10
        MDTextField:
            id: video_path
            hint_text: "Enter video path or browse"
            size_hint: None, None
            width: 400
            height: 40
            pos_hint: {"center_x": .5, "center_y": .8}
        MDRectangleFlatButton:
            text: "Browse"
            pos_hint: {"center_x": .5, "center_y": .7}
            on_release: app.browse_video()
        MDRectangleFlatButton:
            text: "Translate"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_release: app.translate_video()

<HandwrittenTranslatorScreen>:
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Handwritten Text Translator"
            md_bg_color: app.theme_cls.primary_color
            elevation: 10
        MDTextField:
            id: handwritten_path
            hint_text: "Enter handwritten image path or browse"
            size_hint: None, None
            width: 400
            height: 40
            pos_hint: {"center_x": .5, "center_y": .8}
        MDRectangleFlatButton:
            text: "Browse"
            pos_hint: {"center_x": .5, "center_y": .7}
            on_release: app.browse_handwritten()
        MDRectangleFlatButton:
            text: "Translate"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_release: app.translate_handwritten()

<PdfTranslatorScreen>:
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "PDF Text Translator"
            md_bg_color: app.theme_cls.primary_color
            elevation: 10
        MDTextField:
            id: pdf_path
            hint_text: "Enter PDF path or browse"
            size_hint: None, None
            width: 400
            height: 40
            pos_hint: {"center_x": .5, "center_y": .8}
        MDRectangleFlatButton:
            text: "Browse"
            pos_hint: {"center_x": .5, "center_y": .7}
            on_release: app.browse_pdf()
        MDRectangleFlatButton:
            text: "Translate"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_release: app.translate_pdf()
"""
)

class Tab(MDFloatLayout,MDTabsBase):
    pass


class ImageTranslatorScreen(Screen):
    pass


class VideoTranslatorScreen(Screen):
    pass


class HandwrittenTranslatorScreen(Screen):
    pass


class PdfTranslatorScreen(Screen):
    pass


class MainApp(MDApp):



    def build(self):
        self.theme_cls.primary_palette = "DeepOrange"
        self.screen_manager = ScreenManager()

        self.image_translator_screen = ImageTranslatorScreen(name="image_translator_screen")
        self.video_translator_screen = VideoTranslatorScreen(name="video_translator_screen")
        self.handwritten_translator_screen = HandwrittenTranslatorScreen(name="handwritten_translator_screen")
        self.pdf_translator_screen = PdfTranslatorScreen(name="pdf_translator_screen")

        self.screen_manager.add_widget(self.image_translator_screen)
        self.screen_manager.add_widget(self.video_translator_screen)
        self.screen_manager.add_widget(self.handwritten_translator_screen)
        self.screen_manager.add_widget(self.pdf_translator_screen)

        return self.screen_manager
    def browse_image(self):
        self.image_path.text = self.select_file()

    def select_file(self):
        try:
            from tkinter import Tk
            from tkinter.filedialog import askopenfilename
        except ImportError:
            from tkFileDialog import askopenfilename

        Tk().withdraw()
        filename = askopenfilename()
        return filename

    def show_dialog(self, text):
        self.dialog = MDDialog(
            title="Translation",
            text=text,
            size_hint=(0.7, 1),
            buttons=[
                MDRectangleFlatButton(
                    text="OK", on_release=self.close_dialog
                )
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()


if __name__ == "__main__":
    MainApp().run()
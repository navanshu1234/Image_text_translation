from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser
from kivy.core.window import Window
from iv import imv
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivymd.uix.widget import Widget, MDWidget

Window.size = (300, 500)


class FileChooser(MDApp):
    def build(self):
        return Builder.load_string((imv))

    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        if selection:
            self.root.ids.img.source = selection[0]


FileChooser().run()
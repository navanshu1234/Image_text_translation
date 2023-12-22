from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser
from kivy.core.window import Window
from ivvv import imv
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (300, 500)


class ImageScreen(Screen):
    pass

class FileChooser(MDApp):
    def build(self):
        Builder.load_string((imv))
        sm = ScreenManager()
        sm.add_widget(ImageScreen(name='image'))
        return sm

    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        if selection:
            self.root.ids.img.source = selection[0]



FileChooser().run()
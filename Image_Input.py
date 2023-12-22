from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser
from kivy.core.window import Window
from iv import imv


Window.size = (300, 500)


class MT(MDApp):
    def build(self):
        return Builder.load_string(imv)

    def file_chooser1(self):
        filechooser.open_file(on_selection=self.selected1)

    def selected1(self, selection1):
        self.root.ids.img1.source = selection1[0]

MT().run()
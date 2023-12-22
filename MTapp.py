
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from screen_nav import sh
from kivy.core.window import Window


Window.size = (300, 500)

class MenuScreen(Screen):
    pass

class ImageScreen(Screen):
    pass

class CameraScreen(Screen):
    pass

class TextScreen(Screen):
    pass

class FileScreen(Screen):
    pass

class MT(MDApp):
    def build(self):
        Builder.load_string((sh))
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ImageScreen(name='image'))
        sm.add_widget(CameraScreen(name='camera'))
        sm.add_widget(TextScreen(name='ts'))
        sm.add_widget(FileScreen(name='file'))
        return sm


MT().run()
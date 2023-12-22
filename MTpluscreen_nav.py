from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from screen_nav import screen_helper
from kivy.core.window import Window
from plyer import filechooser
from kivymd.uix.toolbar import MDTopAppBar
Window.size = (300, 500)
# Declare both screens
class MenuScreen(Screen):
    pass

class ImageScreen(Screen):
    pass

class CameraScreen(Screen):
    pass

class FileScreen(Screen):
    pass



class TestApp(MDApp):

    def build(self):
        Builder.load_string(screen_helper)
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ImageScreen(name='image'))
        sm.add_widget(CameraScreen(name='camera'))
        sm.add_widget(FileScreen(name='file'))
        return sm





if __name__ == '__main__':
    TestApp().run()
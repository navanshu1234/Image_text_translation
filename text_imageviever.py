from kivymd.app import MDApp
from kivy.lang import builder
from plyer import filechooser
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty,DictProperty,ObjectProperty
kv = """
BoxLayout:
    orientation: 'vertical'

    FloatLayout:
        MDRaisedButton:
            text:"upload"
            pos_hint: {'center_x': 0.5, 'center_y': 0.46}
            on_release:
                app.open_file_manager()


"""

Window.size = (300, 500)

class MT(MDApp):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.file_manager_obj = MDFileManager(
            select_path = self.select_path,
            exit_manager = self.exit_manager,
            preview = True
        )
    def select_path(self,path):
        print(path)
        self.exit_manager()

    def open_file_manager(self):
        self.file_manager_obj.show('/')

    def exit_manager(self):
        self.file_manager_obj.close()

    def build(self):
        Builder.load_string(kv)





MT().run()
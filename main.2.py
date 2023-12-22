from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton,MDRectangleFlatIconButton
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (300, 500)



class MT(MDApp):
      def build(self):
          screen = Screen()
          self.theme_cls.primary_palette = "Gray"
          button1 = MDRectangleFlatIconButton(icon= "file-image",text='Image Input',text_color = (1,1,1,1), md_bg_color = (0,0,0,1),
                                 pos_hint={'center_x': 0.5,'center_y': 0.8},size_hint=(0.5,0.01))
          button2 = MDRectangleFlatIconButton(icon= "camera",text='Camera Image', text_color=(1, 1, 1, 1), md_bg_color=(0,0,0,1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.68},size_hint=(0.5,0.01))
          button3 = MDRectangleFlatIconButton(icon = "file-word-box",text='Enter Text ', text_color=(1, 1, 1, 1), md_bg_color=(0, 0, 0, 1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.56}, size_hint=(0.5, 0.01))
          button4 = MDRectangleFlatIconButton(icon = "file",text='Other File', text_color=(1, 1, 1, 1), md_bg_color=(0, 0, 0, 1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.44}, size_hint=(0.5, 0.01))
          button5 = MDRectangleFlatIconButton(icon= "exit-to-app",text='Exit', text_color=(1, 1, 1, 1), md_bg_color=(0, 0, 0, 1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.32}, size_hint=(0.5, 0.01))
          screen.add_widget(button1)
          screen.add_widget(button2)
          screen.add_widget(button3)
          screen.add_widget(button4)
          screen.add_widget(button5)
          return screen


MT().run()
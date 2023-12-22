from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (300, 500)



class MT(MDApp):
      def build(self):
          screen = Screen()
          self.theme_cls.primary_palette = "Green"
          button1 = MDFlatButton(text='Image Input',text_color = (1,0,0,1), md_bg_color = (0.1,0.5,0.5,1),
                                 pos_hint={'center_x': 0.5,'center_y': 0.8},size_hint=(0.5,0.01))
          button2 = MDFlatButton(text='Camera Image', text_color=(1, 0, 0, 1), md_bg_color=(0.1,0.5,0.5,1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.68},size_hint=(0.5,0.01))
          button3 = MDFlatButton(text='Enter Text ', text_color=(1, 0, 0, 1), md_bg_color=(0.1, 0.5, 0.5, 1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.56}, size_hint=(0.5, 0.01))
          button4 = MDFlatButton(text='Other File', text_color=(1, 0, 0, 1), md_bg_color=(0.1, 0.5, 0.5, 1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.44}, size_hint=(0.5, 0.01))
          button5 = MDFlatButton(text='Exit', text_color=(1, 0, 0, 1), md_bg_color=(0.1, 0.5, 0.5, 1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.32}, size_hint=(0.5, 0.01))
          screen.add_widget(button1)
          screen.add_widget(button2)
          screen.add_widget(button3)
          screen.add_widget(button4)
          screen.add_widget(button5)
          return screen


MT().run()
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
import cv2
from kivy.uix.image import Image
import pytesseract
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from scr1 import screen_helper
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
Window.size = (300, 500)

class SM(ScreenManager):
    pass

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



class MainApp(MDApp):
    def build(self):
        Builder.load_string((screen_helper))
        ScreenManager().add_widget(MenuScreen(name='menu'))
        ScreenManager().add_widget(ImageScreen(name='image'))
        ScreenManager().add_widget(TextScreen(name='ts'))
        ScreenManager().add_widget(FileScreen(name='file'))
        layout = MDBoxLayout(orientation='vertical')
        self.image = Image()
        self.label = MDLabel()
        layout.add_widget(self.image)
        layout.add_widget(self.label)
        self.save_img_button = MDRaisedButton(
            text="Click Here",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(None, None))
        self.save_img_button.bind(on_press=self.take_picture)
        layout.add_widget(self.save_img_button)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0/30.0)
        ScreenManager().add_widget(CameraScreen(layout))
        return ScreenManager()
    def load_video(self, *args):
        ret, frame = self.capture.read()
        self.image_frame = frame
        buffer = cv2.flip(frame,0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer,colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture
    def take_picture(self,*args):
        image_name = "picture_at_2_02.png"
        img = cv2.cvtColor(self.image_frame, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (3,3), 0)
        img = cv2.threshold(img, 0 , 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
        text_data = pytesseract.image_to_string(img, lang='eng', config="--psm 6")
        print(text_data)
        self.label = text_data
        cv2.imshow("cv2 final image",img)
        cv2.imwrite(image_name,self.image_frame)

MainApp().run()
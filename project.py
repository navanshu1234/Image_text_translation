from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix import image
from kivy.clock import Clock
import cv2


class MT(MDApp):
    def build(self):
        layout =  MDBoxLayout(orientation='vertical')
        self.image = Image()
        layout.add_widget(self,image)
        layout.add_widget(MDRaisedButton(
            text="Click here",
            pos_hint = {'center_x':0.5,'center_y':0.5},
            size_hint = (None,None))
        )
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval()
        return layout

    def load_video(self,*args):
        ret, frame = self.capture.read()
        self.image_frame = frame
        buffer = cv2.flip(frame,0).tostring()
        texture = Texture.create(size=(frame.shape[1],frame.shape[0]),colorfmt = 'bgr')
        texture.blit_buffer(buffer,colorfmt='bgr',bufferfmt='ubyte')


MT().run()
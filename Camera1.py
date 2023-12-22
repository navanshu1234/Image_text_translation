from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

class KivyCamera(BoxLayout):
   def __init__(self, **kwargs):
      super(KivyCamera, self).__init__(**kwargs)
      self.img1=Image()
      self.add_widget(self.img1)
      self.capture = cv2.VideoCapture(0)
      Clock.schedule_interval(self.update, 1.0/33.0)

   def update(self, *args):
     ret, frame = self.capture.read()
     if ret:
        buf = cv2.flip(frame, 0).tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt="bgr")
        texture.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")
        self.img1.texture = texture

class CamApp(App):
   def build(self):
         return KivyCamera()

if __name__ == "__main__":
   CamApp().run()
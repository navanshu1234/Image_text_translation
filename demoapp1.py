from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
import cv2
import pytesseract
from googletrans import Translator

Builder.load_string("""
<VideoPlayer>:
    orientation: 'vertical'

    MDToolbar:
        title: 'Video Text Translation'
        left_action_items: [["arrow-left", lambda x: root.back_button()]]
        right_action_items: [["play", lambda x: root.play_button()], ["pause", lambda x: root.pause_button()], ["stop", lambda x: root.stop_button()]]

    Video:
        id: video
        source: 'path/to/video.mp4'
        state: 'stop'
        options: {'eos': 'loop'}

    MDTextField:
        id: original_text
        hint_text: 'Original Text'
        multiline: True
        readonly: True

    MDTextField:
        id: translated_text
        hint_text: 'Translated Text'
        multiline: True
        readonly: True
""")

class VideoPlayer(BoxLayout):
    def back_button(self):
        App.get_running_app().stop()

    def play_button(self):
        video = self.ids.video
        video.state = 'play'
        while True:
            ret, frame = video.read()
            if not ret:
                break
            original = pytesseract.image_to_string(frame)
            translator = Translator()
            translated = translator.translate(original, dest='en')
            self.ids.original_text.text = original
            self.ids.translated_text.text = translated.text
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def pause_button(self):
        self.ids.video.state = 'pause'

    def stop_button(self):
        self.ids.video.state = 'stop'

class VideoTextTranslationApp(App):
    def build(self):
        return VideoPlayer()

if __name__ == '__main__':
    VideoTextTranslationApp().run()

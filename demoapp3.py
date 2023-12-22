from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.lang import Builder
from kivy.core.window import Window
import pytesseract
from googletrans import Translator

Window.size = (400, 600)

Builder.load_string('''
<TranslationScreen>:
    orientation: 'vertical'
    MDToolbar:
        title: 'Image/Video Text Translation'
        left_action_items: [['arrow-left', lambda x: app.stop()]]

    FloatLayout:
        id: main_layout

        Image:
            id: image
            source: ''
            allow_stretch: True
            keep_ratio: True
            size_hint_y: 0.7

        Video:
            id: video
            source: ''
            state: 'stop'
            size_hint_y: 0.7

        MDTextField:
            id: original_text
            hint_text: 'Original Text'
            multiline: True
            readonly: True
            size_hint_y: 0.15

        MDTextField:
            id: translated_text
            hint_text: 'Translated Text'
            multiline: True
            readonly: True
            size_hint_y: 0.15

        MDIconButton:
            icon: 'camera'
            on_press: root.choose_image()
            pos_hint: {'center_x': 0.25, 'center_y': 0.1}

        MDIconButton:
            icon: 'video'
            on_press: root.choose_video()
            pos_hint: {'center_x': 0.75, 'center_y': 0.1}

''')

class TranslationScreen(BoxLayout):

    def choose_image(self):
        from kivy.uix.filechooser import FileChooserListView
        content = FileChooserListView()
        popup = Popup(title="Choose Image", content=content, size_hint=(0.9, 0.9))
        content.path = '.'
        content.on_submit = lambda x: self.set_image(content.selection[0])
        popup.open()

    def choose_video(self):
        from kivy.uix.filechooser import FileChooserListView
        content = FileChooserListView()
        popup = Popup(title="Choose Video", content=content, size_hint=(0.9, 0.9))
        content.path = '.'
        content.on_submit = lambda x: self.set_video(content.selection[0])
        popup.open()

    def set_image(self, image_path):
        self.ids.image.source = image_path
        self.ids.video.source = ''
        self.translate_text(pytesseract.image_to_string(image_path))

    def set_video(self, video_path):
        self.ids.video.source = video_path
        self.ids.image.source = ''
        self.ids.video.state = 'play'
        while True:
            ret, frame = self.ids.video.read()
            if not ret:
                break
            original = pytesseract.image_to_string(frame)
            self.translate_text(original)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def translate_text(self, original):
        translator = Translator()
        translated = translator.translate(original, dest='en')
        self.ids.original_text.text = original
        self.ids.translated_text.text = translated.text

class TranslationApp(App):

    def build(self):
        return TranslationScreen()

if __name__ == '__main__':
    TranslationApp().run()

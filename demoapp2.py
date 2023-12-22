from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
import cv2
import pytesseract
import tensorflow as tf
import PyPDF2

Builder.load_string("""
<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Text Translation'
        MDLabel:
            text: 'Select a translation type'
            halign: 'center'
        MDRaisedButton:
            text: 'Image Text Translation'
            on_release: root.manager.current = 'image'
        MDRaisedButton:
            text: 'Video Text Translation'
            on_release: root.manager.current = 'video'
        MDRaisedButton:
            text: 'Handwritten Text Translation'
            on_release: root.manager.current = 'handwritten'
        MDRaisedButton:
            text: 'PDF Text Translation'
            on_release: root.manager.current = 'pdf'

<ImageScreen>:
    name: 'image'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Image Text Translation'
            left_action_items: [["arrow-left", lambda x: app.root.current='main']]
        MDLabel:
            text: 'Select an image'
            halign: 'center'
        MDRaisedButton:
            text: 'Select Image'
            on_release: root.file_manager_open()
        MDTextField:
            id: image_path
            hint_text: 'Image path'
            readonly: True
        MDRaisedButton:
            text: 'Translate'
            on_release: root.translate()

<VideoScreen>:
    name: 'video'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Video Text Translation'
            left_action_items: [["arrow-left", lambda x: app.root.current='main']]
        MDLabel:
            text: 'Select a video'
            halign: 'center'
        MDRaisedButton:
            text: 'Select Video'
            on_release: root.file_manager_open()
        MDTextField:
            id: video_path
            hint_text: 'Video path'
            readonly: True
        MDRaisedButton:
            text: 'Translate'
            on_release: root.translate()

<HandwrittenScreen>:
    name: 'handwritten'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Handwritten Text Translation'
            left_action_items: [["arrow-left", lambda x: app.root.current='main']]
        MDLabel:
            text: 'Draw a character or word'
            halign: 'center'
        MDIconButton:
            icon: 'pencil'
            on_release: root.start_drawing()
        MDIconButton:
            icon: 'check'
            on_release: root.stop_drawing()
        MDTextField:
            id: handwriting_text
            hint_text: 'Handwriting text'
            readonly: True
        MDRaisedButton:
            text: 'Translate'
            on_release: root.translate()

<PdfScreen>:
    name: 'pdf'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'PDF Text Translation'
            left_action_items: [["arrow-left", lambda x:

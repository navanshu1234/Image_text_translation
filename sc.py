screen_helper = """
ScreenManager:
    MenuScreen:
    ImageScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatIconButton:
        icon:"file-image"
        text:'Image Input'
        text_color: (1, 1, 1, 1) 
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'image'
    MDRectangleFlatIconButton:
        icon: "camera"
        text:'Camera Image'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0,0,0,1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.68}
        size_hint: (0.5,0.01)
        on_press: root.manager.current = 'camera'
    MDRectangleFlatIconButton:
        icon: "file-word-box"
        text: 'Enter Text ' 
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.56}
        size_hint: (0.5, 0.01)
    MDRectangleFlatIconButton:
        icon: "file"
        text: 'Other File' 
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.44}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'file'
    MDRectangleFlatIconButton:
        icon: "exit-to-app"
        text: 'Exit'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.32}
        size_hint: (0.5, 0.01)

<ImageScreen>:
    name: 'image'
    MDRectangleFlatIconButton:
        icon: 'file-image'
        text: 'Back'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.32}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'menu'

<CameraScreen>:
    name: 'Camera'
    MDRectangleFlatIconButton:
        icon: 'file-image'
        text: 'Extract'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.32}
        size_hint: (0.5, 0.01)
    MDRectangleFlatIconButton:
        icon: 'file-image'
        text: 'Back'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.20}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'menu'

<FileScreen>:
    name: 'file'
    MDRectangleFlatIconButton:
        icon: 'file-image'
        text: 'Extract'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.32}
        size_hint: (0.5, 0.01)
    MDRectangleFlatIconButton:
        icon: 'file-image'
        text: 'Back'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.20}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'menu'

"""

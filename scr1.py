screen_helper = """
<ScreenManager>:
    MenuScreen:
        name: 'menu'
    ImageScreen:
        name: 'image'
    CameraScreen:
        name: 'camera'
    TextScreen:
        name: 'ts'
    FileScreen:
        name: 'file'
<MenuScreen>:
    MDTopAppBar:
        id: toolbar
        title: "Image-Text Converter"
        elevation: 4
        pos_hint: {'top': 1}
    MDRectangleFlatIconButton:
        icon:"file-image"
        text:'Image Input'
        text_color: (1, 1, 1, 1) 
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'image'
    MDRectangleFlatIconButton:
        icon: "camera"
        text:'Camera Image'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0,0,0,1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.58}
        size_hint: (0.5,0.01)
        on_press: root.manager.current = 'CameraScreen'
    MDRectangleFlatIconButton:
        icon: "file-word-box"
        text: 'Enter Text ' 
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.46}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'ts'
    MDRectangleFlatIconButton:
        icon: "file"
        text: 'Other File' 
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.34}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'file'
    MDRectangleFlatIconButton:
        icon: "exit-to-app"
        text: 'Exit'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.22}
        size_hint: (0.5, 0.01)
        on_press: app.stop()

<ImageScreen>:
    MDRectangleFlatIconButton:
        icon:"file-image"
        text:'Upload Image'
        text_color: (1, 1, 1, 1) 
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.34}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'file'
    MDRectangleFlatIconButton:
        icon: 'backburger'
        text: 'Back'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.22}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'menu'

<TextScreen>:
    MDRectangleFlatIconButton:
        icon: 'openid'
        text: 'Extract'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.32}
        size_hint: (0.5, 0.01)
    MDRectangleFlatIconButton:
        icon: 'backburger'
        text: 'Back'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.20}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'menu'


<FileScreen>:
    MDRectangleFlatIconButton:
        icon: 'openid'
        text: 'Extract'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.32}
        size_hint: (0.5, 0.01)
    MDRectangleFlatIconButton:
        icon: 'backburger'
        text: 'Back'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.20}
        size_hint: (0.5, 0.01)
        on_press: root.manager.current = 'menu'

"""
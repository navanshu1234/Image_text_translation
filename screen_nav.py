sh = """
ScreenManager:
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
        on_press: root.manager.current = 'camera'
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
    MDFloatLayout:
        orientation: 'vertical'
    
        ScrollView:
            MDGridLayout:
                cols: 2
                adaptive_height: True
                spacing: (10, 15)
                padding: [25, 25]
    
                MDCard:
                    ripple_behavior: True
                    orientation: 'vertical'
                    size_hint_y: None
                    size: 200, 300
                    elevation: 5
                    radius: 5
                    MDIconButton:
                        icon: "camera-outline"
                        user_font_size: "24sp"
                        pos_hint: {"center_x": .5, "center_y": .5}
                    Image:
                        id: img1
                        allow_stretch: True
                        keep_ratio: False
                        # size_hint_y: .5
        MDRectangleFlatIconButton:
            icon:"file-image"
            text:'Upload Image'
            text_color: (1, 1, 1, 1) 
            md_bg_color: (0, 0, 0, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.24}
            size_hint: (0.5, 0.01)
            on_press: root.manager.current = 'file'
        MDRectangleFlatIconButton:
            icon: 'backburger'
            text: 'Back'
            text_color: (1, 1, 1, 1)
            md_bg_color: (0, 0, 0, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.12}
            size_hint: (0.5, 0.01)
            on_press: root.manager.current = 'menu'

<CameraScreen>:
    MDFloatingActionButton:
        icon: 'openid'
        text: 'Extract'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.7, 'center_y': 0.22}

    MDFloatingActionButton:
        icon: 'backburger'
        text: 'Back'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.3, 'center_y': 0.22}
        on_press: root.manager.current = 'menu'

<TextScreen>:
    MDTextField:
        hint_text: "Enter Text"
        pos_hint: {'center_x': 0.5, 'center_y': 0.56}
        multiline: True
        mode: "rectangle"
        helper_text: "Enter text you want to enter"
        helper_text_mode: "on_focus"
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
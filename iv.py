imv = """
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
                    on_release: app.file_chooser1()
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
        pos_hint: {'center_x': 0.5, 'center_y': 0.28}
        size_hint: (0.5, 0.01)
    MDRectangleFlatIconButton:
        icon: 'backburger'
        text: 'Back'
        text_color: (1, 1, 1, 1)
        md_bg_color: (0, 0, 0, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.16}
        size_hint: (0.5, 0.01)     
    
        

"""
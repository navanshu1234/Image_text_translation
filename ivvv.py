imv = """
MDScreenManager:
    ImageScreen:
<ImageScreen>:
    name: 'image'
    MDFloatLayout: 
        Image:
            id: img 
        MDRaisedButton:
            text:"upload"
            pos_hint: {'center_x': 0.5, 'center_y': 0.46}
            on_release:
                app.file_chooser()
        MDLabel:
            id: selected_path
            text: ""
            halign: "center"
"""
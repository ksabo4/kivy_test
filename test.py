import kivymd
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


from kivymd.app import MDApp
#from kivymd.uix.screen import MDScreen
#from kivymd.uix.button import MDRectangleFlatButton


from kivy.lang import Builder


KV = '''
MDScreen:
    BoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "Test 123 Test"
            font_size: 100
        MDLabel:
            text: "Test 123 Test"
            font_size: 50
        MDLabel:
            text: "Test 1 Test"
            font_size: 20
'''
KV2 = '''
MDScreen:

    MDLabel:
            text: "Test2"
            font_size: 10
'''


class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)


Test().run()

"""class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 4
        self.add_widget(Label(text="test", font_size=20))
        self.add_widget(Label(text="test2", font_size=20))
        self.add_widget(Label(text="test3", font_size=20))
        self.add_widget(Label(text="test4", font_size=20))
        self.add_widget(Label(text="test5", font_size=20))


class HealmApp(App):
    def build(self):
        layout = MyGridLayout()
        layout.add_widget(Label(text="test6"))
        return layout


app = HealmApp()
app.run()"""

from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.title='Hệ Thống Quan Trắc Môi Trường'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        Builder.load_file('main.kv')
    def Do(self):
        print("Hello")

MainApp().run()

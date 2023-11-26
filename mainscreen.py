from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# Designate Our .kv design file 
Builder.load_file('mainscreen.kv')

class MyLayout(Widget):
	pass

class AwesomeApp(MDApp):
	def build(self):
		# self.theme_cls.primary_color= "Dark"
		# self.theme_cls.primary_color="DeepPurle"
		self.title = "Quan Trac Moi Truong"

		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()
from kivymd.app import MDApp

class MainApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = 'Amber'

if __name__ == '__main__':
	app = MainApp()
	app.run()
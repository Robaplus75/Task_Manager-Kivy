from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime
from kivy.properties import StringProperty
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox


class DialogContent(MDBoxLayout):
	selected_date = StringProperty()
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.selected_date = datetime.now().strftime("%A %d %B %Y")

	def show_date_picker(self):
		date_dialog = MDDatePicker()
		date_dialog.bind(on_save = self.on_save)
		date_dialog.open()

	def on_save(self, instance, value, date_range):
		date = value.strftime("%A %d %B %Y")
		# self.ids.DialogContent = str(date)
		self.selected_date = str(date)


class ListItemWithCheckbox(TwoLineAvatarIconListItem):
	def __init__(self, pk=None, *args, **kwargs):
		print(f"Text: {kwargs.get('text')}")
		super().__init__(*args, **kwargs)

		self.pk = pk

	def mark(self, check, the_list_item):
		if check.active == True:
			the_list_item.text = f"[s]{the_list_item.text}[/s]"
		else:
			pass

	def delete_item(self, the_list_item):
		self.parent.remove_widget(the_list_item)


class LeftCheckbox(ILeftBody, MDCheckbox):
	pass


class MainApp(MDApp):
	task_list_dialog = None

	def build(self):
		self.theme_cls.primary_palette = 'Teal'

	def show_task_function(self):
		print(f"Show the task, tasklist: {self.task_list_dialog}")
		if not self.task_list_dialog:
			self.task_list_dialog = MDDialog(
				title = "Create Task",
				type = "custom",
				content_cls = DialogContent(),
				on_dismiss=self.on_dialog_dismiss
			)
			self.task_list_dialog.open()
	def close_dialog(self, *args, **kwargs):
		self.task_list_dialog.dismiss()

	def on_dialog_dismiss(self, widget):
		self.task_list_dialog = None

	def add_task(self, task, task_date):
		print(task.text, task_date)
		print("ONE")
		self.root.ids['container'].add_widget(ListItemWithCheckbox(text=f"[b]{task.text}[/b]", secondary_text=task_date))
		print("TWOO")
		task.text = ''


if __name__ == '__main__':
	app = MainApp()
	app.run()
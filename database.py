import sqlite3

class Database():
	def __init__(self):
		self.conn = sqlite3.connect("todo_database.db")
		self.cursor = self.conn.cursor()
		self.create_task_table()

	def create_task_table(self):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id integer PRIMARY KEY AUTOINCREMENT, task varchar(50) NOT NULL, due_date varchar(50) NOT NULL, completed BOOLEAN NOT NULL CHECK (completed IN (0,1)))")
		self.conn.commit()

	def create_task(self, task, due_date):
		self.cursor.execute("INSERT INTO tasks(task, due_date, completed) VALUES(?,?,?)", (task, due_date, 0))
		self.conn.commit()

		created_task = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE task=? and completed=0",(task,)).fetchall()
		return created_task[-1]

	def get_tasks(self):
		incompleted_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed=0").fetchall()
		completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed=1").fetchall()

		return incompleted_tasks, completed_tasks

	def mark_task_as_completed(self, taskid):
		self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id=?", (taskid,))
		self.conn.commit()

		task_text = self.cursor.execute("SELECT task FROM tasks WHERE id=?",(taskid,)).fetchall()
		return task_text[0][0] if task_text else None

	def mark_task_as_incompleted(self, taskid);
		self.cursor.execute("UPDATE tasks SET completed = 0 WHERE id=?", (taskid,))
		self.conn.commit()

		task_text = self.cursor.execute("SELECT task FROM tasks WHERE id=?",(taskid,)).fetchall()
		return task_text[0][0] if task_text else None

	def delete_task(self, taskid):
		self.cursor.execute("DELETE FROM tasks WHERE id=?",(taskid,))
		self.conn.commit()

	def close_db_connection(self):
		self.conn.close()
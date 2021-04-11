from datetime import datetime
from os import path

class ResultFile:
	def __init__(self, file_name, title, operation, result):
		self.file_name = f'{file_name}.md'
		self.title = title
		self.operation = operation
		self.result = result
	
	def save_operation(self):
		date = datetime.today()
		content = (
			f'# {self.title}\n\n' +
			f'> **Date**: {date.day}/{date.month}/{date.year}\n\n' +
			f'**Steps**:\n\n'
			f'${self.operation}$\n\n'
			f'**Result**:\n\n${self.result}$\n'
		)

		file_path = path.join("out", self.file_name)
		try:
			f = open(file_path, "x")
			f.write(content)
			f.close()
		except:
			f = open(file_path, "w")
			f.write(content)
			f.close()

		return file_path

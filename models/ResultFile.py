from datetime import datetime, timedelta
from os import path

class ResultFile:
  def __init__(self, file_name, title, operation, result):
    self.file_name = f'{file_name}.md'
    self.title = title
    self.operation = operation
    self.result = result

  def save_operation(self, add_latex_symbols=True, print_steps=True, latex_expression=""):
    date = datetime.today()
    content = (
      f'# {self.title}\n\n' +
      f'> **Date**: {date.day}/{date.month}/{date.year}  {date.hour}:{date.minute}:{date.second}\n\n' + #ADD HOUR
      f'**Expression**:\n\n ${latex_expression}$\n\n'  +
      ((f'**Steps**:\n\n' + (self.operation if not add_latex_symbols else f'${self.operation}$') + "\n\n") if print_steps == True else '') +
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

    print(f"Calculation is saved. Open the results in {file_path}")

    return file_path



from core.execution_unit.execution_unit import ExecutionUnit
from modules.ms.todo.todo import ToDo, Task


class TODOExecutionUnit(ExecutionUnit):
  def __init__(self, initial_command: str):
    self._todo = ToDo()
    if len(initial_command):
      self._create_task(initial_command)

  def _create_task(self, task_desc):
    todo_task = Task(task_desc)
    # TODO This also should be from user
    list_name = "ForTesting"
    rc = self._todo.addTask(list_name, todo_task)
    self._set_bool_to_status(rc)



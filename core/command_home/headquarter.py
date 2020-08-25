from core.command_home.extractor import Extractor
from core.command_home.commands import Types, Command
from core.execution_unit.execution_unit import ExecutionUnit
from modules.ms.todo.todo import ToDo, Task
from core.execution_unit.unit_status import UnitStatus
import logging

logging.basicConfig(level=logging.INFO)


class Headquarter:
  @staticmethod
  def process(message: str) -> ExecutionUnit:
    exec_unit = ExecutionUnit()
    status = UnitStatus.ERROR
    logging.debug(message)
    command = Extractor.parseCommand(message, None)
    if command.getType() is Types.TODO_CREATE_TODO:
      rc = Headquarter._processToDoTask(command)
      status = UnitStatus.OK if rc else UnitStatus.ERROR

    exec_unit.setStatus(status)
    return exec_unit

  @staticmethod
  def _processToDoTask(command: Command) -> bool:
    todo = ToDo()
    todo_task = Task(command.getData())
    # TODO This also should be from user
    list_name = "ForTesting"
    return todo.addTask(list_name, todo_task)

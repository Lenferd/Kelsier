from core.command_home.extractor import Extractor
from core.command_home.commands import Types, Command
from modules.ms.todo.todo import ToDo, Task
import logging

logging.basicConfig(level=logging.INFO)

class Headquarter:
  @staticmethod
  def process(message: str):
    done = False
    logging.debug(message)
    command = Extractor.parseCommand(message, None)
    if command.getType() is Types.TODO_CREATE_TODO:
      done = Headquarter._processToDoTask(command)

    return done


  @staticmethod
  def _processToDoTask(command: Command) -> bool:
    todo = ToDo()
    todo_task = Task(command.getData())
    # TODO This also should be from user
    list_name = "ForTesting"
    return todo.addTask(list_name, todo_task)

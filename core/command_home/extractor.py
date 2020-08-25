from core.command_home.commands import Command
from core.command_home.commands import Types

# TODO Use active mode and callbacks
# TODO Add tests

class Extractor:
  @staticmethod
  def parseCommand(str_command: str, callback) -> Command:
    where = Extractor._searchWhereToDo(str_command)
    what = Extractor._searchWhatToDo(str_command)
    command = Command(where, what)
    return command

  @staticmethod
  def _searchWhereToDo(string: str):
    # TODO More complicated logic required here
    if string.lower().find("todo") != -1:
      return Types.TODO_CREATE_TODO

  @staticmethod
  def _searchWhatToDo(string: str) -> str:
    # TODO Handle this part more precisely
    return string.split(":")[1]

from core.command_home.available_modules import AvailableModules
import re


class Extractor:
  @staticmethod
  def getModule(str_command: str) -> AvailableModules:
    symbols_to_die = r'[.:!?;]'
    cleaned_str = re.sub(symbols_to_die, ' ', str_command)
    words = cleaned_str.lower().split()

    todo_words = {"todo", "task"}
    one_note_words = {"onenote", "note", "form", "page"}
    if set(words) & set(todo_words):
      return AvailableModules.TODO
    elif set(words) & set(one_note_words):
      return AvailableModules.ONE_NOTE
    return AvailableModules.NOT_FOUND

  # TODO Should it be execution module logic?
  @staticmethod
  def separateCommandFromModule(str_command: str):
    # TODO Handle this part more precisely
    try_split = str_command.split(":")
    command = ""
    if len(try_split) > 1:
      command = try_split[1]
    else:
      ""
    return command

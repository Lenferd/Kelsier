from core.command_home.available_modules import AvailableModules
import re

todo_words = {"todo", "task"}
one_note_words = {"onenote", "note", "form", "page", "template"}


class Extractor:
  @staticmethod
  def getModule(str_command: str) -> AvailableModules:
    symbols_to_die = r'[.:!?;]'
    cleaned_str = re.sub(symbols_to_die, ' ', str_command)
    words = cleaned_str.lower().split()

    if set(words) & set(todo_words):
      return AvailableModules.TODO
    elif set(words) & set(one_note_words):
      return AvailableModules.ONE_NOTE
    return AvailableModules.NOT_FOUND

  # TODO Should it be execution module logic?
  @staticmethod
  def separateCommandFromModule(str_command: str):
    command = Extractor._try_split(str_command)
    if command is not None:
      return command
    command = Extractor._try_replace(str_command)
    if len(command):
      return command
    return ""

  @staticmethod
  def _try_split(str_command: str):
    # TODO Handle this part more precisely
    try_split = str_command.split(":")
    if len(try_split) > 1:
      return try_split[1]
    else:
      return None

  @staticmethod
  def _try_replace(str_command: str):
    try_replace = str_command
    for command in todo_words:
      try_replace = try_replace.replace(command, "")
    for command in one_note_words:
      try_replace = try_replace.replace(command, "")
    return try_replace

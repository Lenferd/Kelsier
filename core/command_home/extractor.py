from core.command_home.available_modules import AvailableModules


class Extractor:
  @staticmethod
  def getModule(str_command: str) -> AvailableModules:
    if str_command.lower().find("todo") != -1:
      return AvailableModules.TODO
    if str_command.lower().find("form") != -1:
      return AvailableModules.ONE_NOTE

  # TODO Should it be execution module logic?
  @staticmethod
  def separateCommandFromModule(str_command: str):
    # TODO Handle this part more precisely
    try_split = str_command.split(":")
    command = ""
    if len(try_split) > 1:
      command = try_split[1]
    else:
      raise Exception("I don't know how to split command :(")
    return command

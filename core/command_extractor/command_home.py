# TODO Use active mode and callbacks
# TODO Add tests

# TODO Make it case insensitive
known_commands = ["Print"]

import datetime


class Errors:
  @staticmethod
  def incorrect_command(command):
    return "Command {} is incorrect. Please try to use command from {}" \
      .format(command, known_commands)


# TODO Add logger
def process(message: str):
  words = message.split()
  print(words)
  command = words[0]
  print("Commnad: {}".format(command))
  action = words[1]
  print("Action: {}".format(action))
  if command in known_commands:
    if action == "time":
      return "Time is {}".format(datetime.datetime.now())
  else:
    return Errors.incorrect_command(command)

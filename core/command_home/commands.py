from enum import Enum

# TODO Didn't found how to do Types.ToDo.CreateToDO
class Types(Enum):
  NOT_INITIALIZED = 0

  TODO_CREATE_TODO = 10


class Command:
  def __init__(self, type: Types, data):
    self._type = type
    self._data = data

  def getType(self):
    return self._type

  def getData(self):
    return self._data

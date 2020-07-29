from modules.ms.microsoft_graph import MicrosoftGraph

class Page:
  def __init__(self, ms: MicrosoftGraph, input_dict: dict):
    self._ms = ms
    self._dict = input_dict
    self._root = input_dict['self']

  def getContent(self):
    print("was here")


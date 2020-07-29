from modules.ms.microsoft_graph import MicrosoftGraph

class Page:
  def __init__(self, ms: MicrosoftGraph, input_dict: dict):
    self._ms = ms
    self._dict = input_dict
    self._root = input_dict['self']
    self._content_query = self._root + "/content"
    self._html = None

  def getContent(self):
    self._html = self._ms.request(self._content_query)
    return self._html

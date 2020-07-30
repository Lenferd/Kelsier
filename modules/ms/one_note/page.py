import json

from modules.ms.microsoft_graph import MicrosoftGraph
from bs4 import BeautifulSoup


class Page:
  def __init__(self, ms: MicrosoftGraph, input_dict: dict):
    self._ms = ms
    self._dict = input_dict
    self._root = input_dict['self']
    self._content_get = self._root + "/content?includeIDs=true"
    self._content_post = self._root + "/content"
    self._html = None
    self._paragraphs = []

  def getText(self):
    self._html = self._ms.request(self._content_get)
    soup = BeautifulSoup(self._html, "html.parser")
    return soup.find("div").text

  def getParagraphs(self):
    self._html = self._ms.request(self._content_get)
    soup = BeautifulSoup(self._html, "html.parser")
    for p in soup.find_all("p"):
      self._paragraphs.append({"id": p.attrs['id'], "text": p.text})
    return self._paragraphs

  def _replaceRequest(self, content: dict, operation="replace"):
    return [{
      'target': content['id'],
      'action': operation,
      'content': content['text']
    }]

  def updateContent(self, newContent: dict):
    data = self._replaceRequest(newContent)
    response = self._ms.path(self._content_post, data)
    if response is None:
      raise Exception("Failed to update content")

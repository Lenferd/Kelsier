from modules.ms.microsoft_graph import MicrosoftGraph
from modules.ms.one_note.page import Page
from utils.search import *

class Section:
  def __init__(self, ms: MicrosoftGraph, input_dict: dict):
    self._ms = ms
    self._dict = input_dict
    self._root = input_dict['self']
    self._pages_query = "/pages"

  def _getAllPages(self):
    all_pagess_query = self._root + self._pages_query
    pages = self._ms.request(all_pagess_query)['value']
    return pages

  def getPage(self, page_name: str):
    pages = self._getAllPages()
    found_page = searchDictInListOfDict(pages, "title", page_name)
    if found_page is not None:
      return Page(self._ms, found_page)
    else:
      return None

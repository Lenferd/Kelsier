from modules.ms.microsoft_graph import MicrosoftGraph
from modules.ms.one_note.section import Section
from utils.search import *


class Notebook:
  def __init__(self, ms: MicrosoftGraph, input_dict: dict):
    self._ms = ms
    self._dict = input_dict
    self._root = input_dict['self']
    self._section_query = "/sections"

  def _getAllSections(self):
    all_sections_query = self._root + self._section_query
    sections = self._ms.request(all_sections_query)['value']
    return sections

  def getSection(self, section_name: str):
    sections = self._getAllSections()
    found_section = searchDictInListOfDict(sections, "displayName",
                                           section_name)
    if found_section is not None:
      return Section(self._ms, found_section)
    else:
      return None

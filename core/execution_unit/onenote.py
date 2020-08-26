import re
from enum import Enum

from core.execution_unit.execution_unit import ExecutionUnit
from modules.ms.one_note.one_note import OneNote
from core.execution_unit.unit_status import UnitStatus

class Mode(Enum):
  MODE_NOT_FOUND = -1

  FILL_TEMPLATE=10
  FILL_PAGE=11
  READ_PAGE=12


def _get_exec_mode(initiation):
  if initiation.find("fill form") != -1:
    return Mode.FILL_TEMPLATE
  if initiation.find("fill page") != -1:
    return Mode.FILL_PAGE
  return Mode.MODE_NOT_FOUND


class OneNoteExecutionUnit(ExecutionUnit):
  def __init__(self, initial_command: str):
    self._oneNote = OneNote()
    # TODO Should not be hardcoded
    self._notebookName = "TestNotebook"
    self._sectionName = "TestSection"
    self._pageName = "TemplatePage"

    self._execution_mode = _get_exec_mode(initial_command)
    self._status = UnitStatus.HAVE_QUESTION
    self._page = self._oneNote.getPage(self._notebookName,
                                       self._sectionName,
                                       self._pageName)
  #   Template scenario
    self._index = 0
    self._paragraphs = self._page.getParagraphs()

  # TODO Use dicts?
  def execute(self, instructions):
    if instructions.find("get") != -1:
      # TODO very tricky
      return self._paragraphs[self._index]['text']
    if len(instructions):
      if self._execution_mode == Mode.FILL_TEMPLATE:
        self._fill_answer(instructions, self._index)
      if self._execution_mode == Mode.FILL_PAGE:
        self._fill_line(instructions, self._index)
      self._index += 1


  # TODO Return class, which can be user to provide answer
  def getQuestion(self):
    if self._status != UnitStatus.HAVE_QUESTION:
      return None
    else:
      text = self._paragraphs[self._index]
      return text['text'].split(":")[0]

  def _fill_answer(self, text, index):
    paragraphs = self._page.getParagraphs()
    updated_paragraph = paragraphs[index]
    if updated_paragraph['text'].find("{") == -1 : return
    updated_paragraph['text'] = re.sub(r'(.*){(.*)}', r'\g<1>', updated_paragraph['text'])
    updated_paragraph['text'] += text
    self._page.updateContent(updated_paragraph)

  def _fill_line(self, text, index):
    paragraphs = self._page.getParagraphs()
    updated_paragraph = paragraphs[index]
    updated_paragraph['text'] = text
    self._page.updateContent(updated_paragraph)






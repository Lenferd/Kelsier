from core.execution_unit.execution_unit import ExecutionUnit
from modules.ms.one_note.one_note import OneNote
from core.execution_unit.unit_status import UnitStatus


class OneNoteExecutionUnit(ExecutionUnit):
  def __init__(self, initial_command: str):
    self._oneNote = OneNote()
    # TODO Should not be hardcoded
    self._notebookName = "TestNotebook"
    self._sectionName = "TestSection"
    self._pageName = "TemplatePage"

    if len(initial_command):
      raise Exception("Initial command not supported")
    self._status = UnitStatus.HAVE_QUESTION
    self._page = self._oneNote.getPage(self._notebookName,
                                       self._sectionName,
                                       self._pageName)
  #   Template scenario
    self._question_index = 0
    self._paragraphs = self._page.getParagraphs()

  def execute(self, instructions):
    if len(instructions):
      self._question_index += 1

  # TODO Return class, which can be user to provide answer
  def getQuestion(self):
    if self._status != UnitStatus.HAVE_QUESTION:
      return None
    else:
      text = self._paragraphs[self._question_index]
      return text['text'].split(":")[0]





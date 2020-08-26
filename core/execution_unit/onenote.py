import re
from enum import Enum
import logging

from core.execution_unit.execution_unit import ExecutionUnit
from modules.ms.one_note.one_note import OneNote
from core.execution_unit.unit_status import UnitStatus
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Mode(Enum):
  MODE_NOT_FOUND = -1

  FILL_TEMPLATE=10
  FILL_PAGE=11
  READ_PAGE=12


def _get_exec_mode(initiation):
  initiation = initiation.strip()
  template_modes = {"fill form", "fill template"}
  if {initiation} & set(template_modes):
    logger.info("Mode: Template")
    return Mode.FILL_TEMPLATE
  if initiation.find("fill page") != -1:
    logger.info("Mode: Fill page")
    return Mode.FILL_PAGE
  logger.info("Mode not determined. Init line \"{}\"".format(initiation))
  return Mode.MODE_NOT_FOUND


class OneNoteExecutionUnit(ExecutionUnit):
  def __init__(self, initial_command: str):
    logger.info(
      '\t= Initialization of executor with command "{}"'.format(initial_command))
    self._oneNote = OneNote()
    # TODO Should not be hardcoded
    self._notebookName = "TestNotebook"
    self._sectionName = "TestSection"
    self._pageName = self._get_page_name(initial_command)

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
    logger.info("Execute: {}".format(instructions))
    if instructions.find("get") != -1:
      logger.info("Get line command, index {}".format(self._index))
      # TODO very tricky
      return self._paragraphs[self._index]['text']
    if len(instructions):
      action = "None"
      if self._execution_mode == Mode.FILL_TEMPLATE:
        self._fill_answer(instructions, self._index)
        action = "Fill template"
      if self._execution_mode == Mode.FILL_PAGE:
        self._fill_line(instructions, self._index)
        action = "Fill page"
      logger.info("{}: {} at line {}".format(action, instructions, self._index))
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
    match = r"(.*?)[{[(<](.*)[]})>]"
    print(updated_paragraph['text'])
    updated_paragraph['text'] = re.sub(match, r'\g<1>', updated_paragraph['text'])
    print(updated_paragraph['text'])
    updated_paragraph['text'] += text
    self._page.updateContent(updated_paragraph)

  def _fill_line(self, text, index):
    paragraphs = self._page.getParagraphs()
    updated_paragraph = paragraphs[index]
    updated_paragraph['text'] = text
    self._page.updateContent(updated_paragraph)

  def _get_page_name(self, initial_command):
    default = "TemplatePage"
    if len(initial_command) == 0 or len(initial_command.split(":")) == 1:
      return default
    split = initial_command.split(":")
    if len(split[1]) == 0:
      return default
    return split[1]






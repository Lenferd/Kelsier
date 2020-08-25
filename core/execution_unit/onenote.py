from core.execution_unit.execution_unit import ExecutionUnit
from modules.ms.one_note.one_note import OneNote
from core.execution_unit.unit_status import UnitStatus


class OneNoteExecutionUnit(ExecutionUnit):
  def __init__(self, initial_command: str):
    self._oneNote = OneNote()
    if len(initial_command):
      raise Exception("Initial command not supported")
    self._status = UnitStatus.READY_TO_WORK


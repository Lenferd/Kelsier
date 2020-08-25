from core.execution_unit.unit_status import UnitStatus


class ExecutionUnit:
  def __init__(self):
    self._status = UnitStatus.OK

  def execute(self, instructions):
    raise Exception("Not implemented")

  def setStatus(self, status: UnitStatus):
    self._status = status

  def getStatus(self) -> UnitStatus:
    return self._status

  def _set_bool_to_status(self, status: bool):
    self._status = UnitStatus.OK if True else UnitStatus.ERROR

  def getQuestion(self):
    raise Exception("Not implemented")

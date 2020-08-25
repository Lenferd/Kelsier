from core.execution_unit.unit_status import UnitStatus


class ExecutionUnit:
  def __init__(self):
    self._status = UnitStatus.OK

  def execute(self, instructions):
    pass

  def setStatus(self, status: UnitStatus):
    self._status = status

  def getStatus(self) -> UnitStatus:
    return self._status

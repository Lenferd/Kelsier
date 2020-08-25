
class ExecutionUnit:
  def __init__(self):
    self._status = True

  def step(self, instructions):
    pass

  def setStatus(self, status: bool):
    self._status = status

  def getStatus(self):
    return self._status

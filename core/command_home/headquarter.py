from core.command_home.extractor import Extractor
from core.command_home.available_modules import AvailableModules
from core.execution_unit.execution_unit import ExecutionUnit
from core.execution_unit.todo import TODOExecutionUnit
from core.execution_unit.unit_status import UnitStatus
import logging

logging.basicConfig(level=logging.INFO)


class Headquarter:
  @staticmethod
  def process(message: str) -> ExecutionUnit:
    logging.debug(message)

    module = Extractor.getModule(message)
    command = Extractor.separateCommandFromModule(message)
    # TODO ask modules, does execution command looks logic for them,
    #  or user should provide more information.
    if module == AvailableModules.TODO:
      return TODOExecutionUnit(command)
    if module == AvailableModules.ONE_NOTE:
      return


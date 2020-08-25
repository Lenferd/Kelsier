from unittest import TestCase
from core.command_home.headquarter import Headquarter
from core.execution_unit.unit_status import UnitStatus


class TestHeadquarters(TestCase):
  def test_can_execute_create_todo_command(self):
    head = "create todo:"
    tail = "test todo from headquarters"
    exec_unit = Headquarter.process(head + tail)

    self.assertEqual(exec_unit.getStatus(), UnitStatus.OK)

  def test_can_initiate_interactive_process(self):
    initiate = "fill form"
    exec_unit = Headquarter.process(initiate)
    self.assertEqual(exec_unit.getStatus(), UnitStatus.READY_TO_WORK)


  def test_can_execute_fill_form_command(self):
    pass

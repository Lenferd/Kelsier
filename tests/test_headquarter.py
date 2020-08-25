from unittest import TestCase
from core.command_home.headquarter import Headquarter


class TestHeadquarters(TestCase):
  def test_can_execute_create_todo_command(self):
    head = "create todo:"
    tail = "test todo from headquarters"
    exec_unit = Headquarter.process(head + tail)
    self.assertEqual(exec_unit.getStatus(), True)

  def test_can_execute_fill_form_command(self):
    initiate = "fill form"
    exec_unit = Headquarter.process(initiate)


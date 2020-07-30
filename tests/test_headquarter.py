from unittest import TestCase
from core.command_home.headquarter import Headquarter


class TestHeadquarters(TestCase):
  def test_can_execute_create_todo_comamnd(self):
    head = "create todo:"
    tail = "test todo from headquarters"
    self.assertEqual(Headquarter.process(head + tail), True)

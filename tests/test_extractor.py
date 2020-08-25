from unittest import TestCase
from core.command_home.extractor import Extractor
from core.command_home.available_modules import AvailableModules


class TestExtractor(TestCase):
  def setUp(self) -> None:
    self.extractor = Extractor()

  def test_todo_module_default(self):
    expected_module = AvailableModules.TODO
    str_command = "create todo:"

    module = self.extractor.getModule(str_command)
    self.assertEqual(expected_module, module)

  def test_todo_module_no_case_sensitive(self):
    expected_module = AvailableModules.TODO
    str_command = "Create TODO:"

    module = self.extractor.getModule(str_command)
    self.assertEqual(expected_module, module)

  def test_todo_extract_command(self):
    expected_module = AvailableModules.TODO
    str_module = "Create TODO:"
    str_command = "Task 1"

    full_command = str_module + str_command
    module = self.extractor.getModule(full_command)
    command = self.extractor.separateCommandFromModule(full_command)
    self.assertEqual(expected_module, module)
    self.assertEqual(str_command, command)

  #   TODO Implement
  def test_todo_can_split_without_two_dots(self):
    pass
    expected_module = AvailableModules.TODO
    str_command = "Create TODO Task Name"


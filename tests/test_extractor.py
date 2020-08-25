from unittest import TestCase
from core.command_home.extractor import Extractor
from core.command_home.commands import Types


class TestExtractor(TestCase):
  def test_extract_todo_creation_command(self):
    expected_data = "Test todo"
    str_command = "create todo:" + expected_data
    # "Create todo: Test todo"
    # "Create TODO Test todo"

    extractor = Extractor()
    command = extractor.parseCommand(str_command, None)

    expected_command = Types.TODO_CREATE_TODO
    self.assertEqual(command.getType(), expected_command)
    self.assertEqual(command.getData(), expected_data)



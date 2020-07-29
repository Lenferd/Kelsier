from unittest import TestCase
from modules.ms.todo.todo import ToDo, Task

class TestToDo(TestCase):
  def setUp(self) -> None:
    self.todo = ToDo()
    self.listName = "ForTesting"

  def test_can_create_task(self):
    task = Task("Remove me!")
    self.assertTrue(self.todo.addTask(self.listName, task))


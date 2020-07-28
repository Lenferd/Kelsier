from unittest import TestCase
from modules.microsoft_graph.microsoft_graph import MicrosoftToDo, Task
import unittest

# TODO remove me
def get_testing_list():
  todo = MicrosoftToDo()
  tasks_url = "https://graph.microsoft.com/beta/me/todo/lists"
  response = todo.request(tasks_url)

  task_id = None
  for task_list in response['value']:
    if task_list["displayName"] == "ForTesting":
      task_id = task_list["id"]

  return "{}/{}/{}".format(tasks_url, task_id, "tasks")


class TestMicrosoftToDo(TestCase):
  def setUp(self) -> None:
    self.todo = MicrosoftToDo()
    self.task_list_url = get_testing_list()

  def test_can_create_task(self):
    # TODO add test for task
    task = Task("Remove me!")
    self.assertIsNotNone(self.todo.post(self.task_list_url, task.get_dict()))

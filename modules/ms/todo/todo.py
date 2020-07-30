from modules.ms.microsoft_graph import MicrosoftGraph
from modules.ms.todo.task import Task


class ToDo:
  def __init__(self):
    self._ms = MicrosoftGraph()
    self._task_lists_url = "https://graph.microsoft.com/beta/me/todo/lists"

  def _searchForListUrl(self, list_name: str):
    # TODO check returned data
    task_lists = self._ms.request(self._task_lists_url)['value']
    found_list = next((list_item for list_item in task_lists if
                       list_item["displayName"] == list_name), None)
    if found_list is not None:
      return "{}/{}/tasks".format(self._task_lists_url, found_list['id'])
    return None

  def addTask(self, list_name: str, task: Task):
    task_list_url = self._searchForListUrl(list_name)
    if task_list_url is None:
      return False

    response = self._ms.post(task_list_url, task.get_dict())
    # TODO parse result of response?
    if response is not None:
      return True


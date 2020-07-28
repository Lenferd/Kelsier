import atexit
import logging
import yaml
import requests
import msal
import json
import os

# Optional logging
logging.basicConfig(level=logging.INFO)
# logging.getLogger("msal").setLevel(logging.INFO)  # Optionally disable MSAL DEBUG logs

stream = open('oauth_settings.yml', 'r')
config = yaml.load(stream, yaml.SafeLoader)


def format_json(json_obj):
  # FIXME Stupid as f
  to_dump_again = json.loads(json_obj)
  return json.dumps(to_dump_again, indent=2)


class MicrosoftToDo:
  def __init__(self):
    self._cache = None
    self._access_token = None
    self._load_cache(config["token_name"])
    self._auth()
    self.req_headers = {
      'Authorization': 'Bearer ' + self._access_token,
      'Accept': '*/*',
      'Content-Type': 'application/json'
    }

  ## Also hide callback to save new token
  def _load_cache(self, token_name: str):
    cache = msal.SerializableTokenCache()
    if os.path.exists(token_name):
      cache.deserialize(open(token_name, "r").read())

    atexit.register(lambda:
                    open(token_name, "w").write(cache.serialize())
                    if cache.has_state_changed else None
                    )
    self._cache = cache

  def _auth(self):
    ms_api = msal.PublicClientApplication(
      config["client_id"], authority=config["authority"],
      token_cache=self._cache
    )
    result = None
    accounts = ms_api.get_accounts()
    if accounts:
      logging.debug("Account found")
      if len(accounts) > 1:
        logging.error("More the one account. First will be used anyway")

      result = ms_api.acquire_token_silent(config["scope"], account=accounts[0])

    if not result:
      logging.info(
        "No suitable token exists in cache. Let's get a new one from AAD.")

      flow = ms_api.initiate_device_flow(scopes=config["scope"])
      if "user_code" not in flow:
        raise ValueError(
          "Fail to create device flow. Err: {}".format(
            json.dumps(flow, indent=4)))

      print(flow["message"])

      result = ms_api.acquire_token_by_device_flow(flow)

    if "access_token" in result:
      self._access_token = result['access_token']
    else:
      logging.error(result.get("error"))
      logging.error(result.get("error_description"))
      logging.error(result.get("correlation_id"))

  def _is_response_ok(self, response):
    if type(response) is not requests.Response:
      # TODO Move it under try-catch block
      logging.error("Incorrect request: {}".format(json.dumps(response, indent=2)))
      return False
    if response.ok:
      logging.debug(
        "Response: {}".format(json.dumps(response.json(), indent=2)))
      return True
    else:
      logging.error("Failed to get response {}".format(
        json.dumps(response.json(), indent=2)))
      return False

  def request(self, url):
    response = requests.get(
      url,
      headers=self.req_headers,
    )
    if self._is_response_ok(response):
      return response.json()
    else:
      return None

  def post(self, url, json_data):
    # TODO dict, not a json as an input, what the heck
    response = requests.post(
      url, headers=self.req_headers,
      json=json_data)
    if self._is_response_ok(response):
      return response.json()
    else:
      return None



class Task:
  def __init__(self, title: str):
    self._title = title
    self._importance = 'normal'
    self._isReminderOn = 'false'  # reminders for looser
    self._status = 'notStarted'

  def get_json(self):
    return json.dumps(self.get_dict())

  def get_dict(self):
    return {
      'title': self._title,
      'importance': self._importance,
      'isReminderOn': self._isReminderOn,
      'status': self._status
    }


if __name__ == '__main__':
  todo = MicrosoftToDo()
  tasks_url = "https://graph.microsoft.com/beta/me/todo/lists"
  response = todo.request(tasks_url)

  # Fixme searching for Zadachi field can be simplified
  task_id = None
  for task_list in response['value']:
    if task_list["displayName"] == "Задачи":
      task_id = task_list["id"]

  task_list_url = "{}/{}/{}".format(tasks_url, task_id, "tasks")

  response = todo.request(task_list_url)
  task = Task("Remove me!")
  print(format_json(task.get_json()))
  response = todo.post(task_list_url, task.get_dict())
  print(response)


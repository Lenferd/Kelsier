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


class MicrosoftGraph:
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

  def _is_json(self, headers):
    return 'application/json' in headers['Content-Type']

  # TODO Overcomplicated, simplify things
  def _is_response_ok(self, response):
    if type(response) is not requests.Response:
      # TODO Move it under try-catch block
      logging.error("Incorrect request: {}".format(json.dumps(response, indent=2)))
      return False
    if response.ok:
      if self._is_json(response.headers):
        json_response = response.json()
        logging.debug(
          "Response: {}".format(json.dumps(json_response, indent=2)))
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
      if self._is_json(response.headers):
        return response.json()
      else:
        return response.text
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

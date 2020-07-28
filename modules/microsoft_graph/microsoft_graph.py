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


class MicrosoftToDo:
  def __init__(self):
    self._cache = None
    self._access_token = None
    self._load_cache(config["token_name"])
    self._auth()

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
      logging.info("No suitable token exists in cache. Let's get a new one from AAD.")

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

  def request(self, url):
    req_headers = {
      'Authorization': 'Bearer ' + self._access_token,
      'Accept': '*/*',
      'Content-Type': 'application/json'
    }
    response = requests.get(
      url,
      headers=req_headers,
    ).json()
    logging.debug("Response: {}".format(json.dumps(response, indent=2)))
    return response


if __name__ == '__main__':
  todo = MicrosoftToDo()
  simple_request = "https://graph.microsoft.com/beta/me"
  response = todo.request(simple_request)
  print("Response: {}".format(json.dumps(response, indent=2)))


import atexit
import logging
import yaml
import requests
import msal
import json
import os

# Optional logging
# logging.basicConfig(level=logging.DEBUG)  # Enable DEBUG log for entire script
# logging.getLogger("msal").setLevel(logging.INFO)  # Optionally disable MSAL DEBUG logs

stream = open('oauth_settings.yml', 'r')
config = yaml.load(stream, yaml.SafeLoader)


## Also hide callback to save new token
def load_cache(token_name: str):
  cache = msal.SerializableTokenCache()
  if os.path.exists(token_name):
    cache.deserialize(open(token_name, "r").read())

  atexit.register(lambda:
                  open(token_name, "w").write(cache.serialize())
                  if cache.has_state_changed else None
                  )
  return cache

#FIXME Clean up this shit
if __name__ == '__main__':
  token = load_cache(config["token_name"])

  ms_api = msal.PublicClientApplication(
    config["client_id"], authority=config["authority"],
    token_cache=token
  )

  accounts = ms_api.get_accounts()
  if len(accounts) > 1:
    logging.error("More the one account. First will be used anyway")

  result = ms_api.acquire_token_silent(config["scope"], account=accounts[0])

  if not result:
    logging.info(
      "No suitable token exists in cache. Let's get a new one from AAD.")

    flow = ms_api.initiate_device_flow(scopes=config["scope"])
    if "user_code" not in flow:
      raise ValueError(
        "Fail to create device flow. Err: {}".format(json.dumps(flow, indent=4)))

    print(flow["message"])

    result = ms_api.acquire_token_by_device_flow(flow)

  if "access_token" in result:
    # Calling graph using the access token
    graph_data = requests.get(  # Use token to call downstream service
      config["endpoint"],
      headers={'Authorization': 'Bearer ' + result['access_token']}, ).json()
    print("Graph API call result: {}".format(json.dumps(graph_data, indent=2)))
  else:
    print(result.get("error"))
    print(result.get("error_description"))
    print(
      result.get("correlation_id"))  # You may need this when reporting a bug

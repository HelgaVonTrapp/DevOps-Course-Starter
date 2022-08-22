#from urllib import response
#from cgitb import reset
#from urllib import response
#from urllib import response
import requests
import json
def get_items():
   
  url = "https://api.trello.com/1/boards/62f2b96de0b99c00aff27ae6/lists?"

  headers = {
    "Accept": "application/json"
    }
 
  query = {
    'key': 'xx',
    'token': 'xx',
    'cards': 'open',
    'card_fields':'name'
    }
 
  response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query,
    )
  
  print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
get_items()

#def add_item():
# url = "https://api.trello.com/1/boards/62f2b96de0b99c00aff27ae6/lists?"

# headers = {
#   "Accept": "application/json"
#  }

# query = {
#   'name': '{name}',
#   'key': 'APIKey',
#   'token': 'APIToken'
#  }

# response = requests.request(
#   "POST",
#   url,
#   headers=headers,
#   params=query
#  )

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
#add_item()

#from urllib import response
#from cgitb import reset
#from urllib import response
#from urllib import response
import requests
import json
import os
from dotenv import load_dotenv

def get_items():
   
  url = "https://api.trello.com/1/boards/62f2b96de0b99c00aff27ae6/lists?"

  headers = {
    "Accept": "application/json"
    }
  load_dotenv()
  trello_key=(os.getenv('TRELLO_KEY'))
  trello_token=(os.getenv('TRELLO_TOKEN'))
  query = {

    'key':trello_key,
    'token':trello_token,
    'cards': 'open',
    'card_fields':'name'
    }
 
  response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query,
    )
  #Create a new array
  apiItems = []
  #Convert json response to a dictionary item
  aDict = json.loads(response.text)
  #Creating a list from a dictionary item and using in the for statement
  for list in aDict:
    for card in list['cards']:
      apiItems.append({"id": card["id"], "title": card["name"], "status": list["name"]})
  #returnng array of data
  return apiItems.copy()

  #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
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

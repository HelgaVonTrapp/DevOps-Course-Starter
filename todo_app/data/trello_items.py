import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
trello_key=(os.getenv('TRELLO_KEY'))
trello_token=(os.getenv('TRELLO_TOKEN'))
trello_todo_list=(os.getenv('TRELLO_TODO_LIST'))
trello_done_list=(os.getenv('TRELLO_DONE_LIST'))
trello_board_url=(os.getenv('TRELLO_BOARD_URL'))

def get_items():   
  url = trello_board_url
  headers = {
    "Accept": "application/json"
    }
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
  apiItems = []
  aDict = json.loads(response.text)
  for list in aDict:
    for card in list['cards']:
      apiItems.append({"id": card["id"], "title": card["name"], "status": list["name"]})
  return apiItems.copy()

def add_item(title):
  url = "https://api.trello.com/1/cards"

  headers = {
   "Accept": "application/json"
  }
  query = {
   'idList': trello_todo_list,
   'key': trello_key,
   'token': trello_token,
   'name': title
  }
  response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
  )

def update_item(id):
  url = f"https://api.trello.com/1/cards/{id}" 

  headers = {
   "Accept": "application/json"
  }
  query = {
   'idList': trello_done_list,
   'key': trello_key,
   'token': trello_token,
   'id': id
  }
  response = requests.request(
    "PUT",
    url,
    headers=headers,
    params=query
  )
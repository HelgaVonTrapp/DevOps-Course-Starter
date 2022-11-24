import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
trello_key=(os.getenv('TRELLO_KEY'))
trello_token=(os.getenv('TRELLO_TOKEN'))
#Get Trello items
def get_items():
   
  url = "https://api.trello.com/1/boards/62f2b96de0b99c00aff27ae6/lists?"

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
#Create a new array
  apiItems = []
#Convert json response to a dictionary item
  aDict = json.loads(response.text)
#Creating a list from a dictionary item and using in the for statement
  for list in aDict:
    for card in list['cards']:
      apiItems.append({"id": card["id"], "title": card["name"], "status": list["name"]})
#returning array of data
  return apiItems.copy()

#Add new item to Trello To Do List
def add_item(title):
  url = "https://api.trello.com/1/cards"

  headers = {
   "Accept": "application/json"
  }

  query = {
   'idList': '62f2b96de0b99c00aff27aed',
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
#find id as variable
def update_item(id):
  url = f"https://api.trello.com/1/cards/{id}" 

  headers = {
   "Accept": "application/json"
  }
#Move to done status, this is the id of done list
  query = {
   'idList': '62f2b96de0b99c00aff27aef',
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
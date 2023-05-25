import requests
import json
import os
import pymongo
#from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
mongo_connection=(os.getenv('MONGO_CONNECTION_STRING'))
mongo_db=(os.getenv('MONGO_DB_NAME'))

client = pymongo.MongoClient(mongo_connection)
#print(client.list_database_names())
database = client['todoapp-DB']
#print(database.list_collection_names())


def get_items():   
  headers = {
    "Accept": "application/json"
    }
collection = database['todoapp-Collection']
documents = list(collection.find())
print(documents)

#response = requests.request(
#    "GET",
#    url,
#    headers=headers,
#    params=query,
 #   )
#apiItems = []
#aDict = json.loads(documents.text)
#for list in aDict:
#    for card in list['cards']:
#      apiItems.append({"id": card["id"], "title": card["name"], "status": list["name"]})
#return apiItems.copy()

def add_item(title):
#  url = "https://api.trello.com/1/cards"

  headers = {
   "Accept": "application/json"
  }
  #query = {
  # 'idList': trello_todo_list,
  # 'key': trello_key,
  # 'token': trello_token,
 #  'name': title
 # }
collection.insert_one({"title":"to-do 4","description":"to-do 4 description","status":"Not Started"})
response = requests.request(
#"POST",
    #url,
    #headers=headers,
    #params=query
  )

def update_item(id):
  for doc in documents.find({}):
    print(doc)
#  url = f"https://api.trello.com/1/cards/{id}" 

  headers = {
   "Accept": "application/json"
  }
#  query = {
#   'idList': trello_done_list,
#   'key': trello_key,
#   'token': trello_token,
#   'id': id
#  }
  response = requests.request(
#    "PUT",
#    url,
#    headers=headers,
#    params=query
  )
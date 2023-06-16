import collections
from turtle import title
from typing import Collection
from unittest import result
import requests
import json
import os
import pymongo
from dotenv import load_dotenv
load_dotenv()

mongo_connection=(os.getenv('MONGO_CONNECTION_STRING'))
mongo_db=(os.getenv('MONGO_DB_NAME'))

client = pymongo.MongoClient(mongo_connection)
database = client['todoapp-DB']

def get_items():  
  collection = database['todoapp-Collection']
  documents = list(collection.find())
  print(documents)
  return documents

def add_item(title,description):
  collection = database['todoapp-Collection']
  collection.insert_one({"title":title,"description":description,"status":"Not Started"})

def update_item(id):
  collection = database['todoapp-Collection']
  collection.update_one({"_id":id},{"$set":{"status":"Complete"}})


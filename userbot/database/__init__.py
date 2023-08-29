from pymongo import MongoClient

class Database:
  def __init__(self):
    self.client = MongoClient('mongodb://141.98.115.181:27017/')
  def insert_data(self, user_id, col, vars):
    self.DATABASE = self.client[str(user_id)]
    result = self.DATABASE[col].insert_one(vars)
    return result.inserted_id

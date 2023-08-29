from pymongo import MongoClient

class Database:
  def __init__(self, user_id):
    self.user_id = user_id
    self.client = MongoClient('mongodb://141.98.115.181:27017/')
    self.DATABASE = self.client[str(self.user_id)]
  def insert_data(self, col, vars):
    result = self.DATABASE[col].insert_one(vars)
    return result.inserted_id

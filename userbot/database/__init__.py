from pymongo import MongoClient

class Database:
  def __init__(x):
    x.client = MongoClient('mongodb://141.98.115.181:27017/')
  def insert_data(x, col, vars):
    result = x.DATABASE[col].insert_one(vars)
    return result.inserted_id
  def initialize_db(x, user_id):
    x.DATABASE = x.client[str(user_id)]
  def get_data(x, col, query):
    result = x.DATABASE[col].find_one(query)
    return result

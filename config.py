from os import environ
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = environ.get("API_ID", "")
API_HASH = environ.get("API_HASH", "")
SESSION_STRING = environ.get("SESSION_STRING", "")

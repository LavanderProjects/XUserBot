from pyrogram import Client
from config import API_ID, API_HASH, SESSION_STRING

app = Client(
  "XUserBot",
  api_id = int(API_ID),
  api_hash = API_HASH,
  session_string = SESSION_STRING,
  plugins = dict(root="userbot.modules"))

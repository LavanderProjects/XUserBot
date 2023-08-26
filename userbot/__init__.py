from pyrogram import Client
from config import API_ID, API_HASH, SESSION_STRING

app = Client(
  name = "XUserBot",
  api_id = API_ID,
  api_hash = API_HASH,
  session_string = SESSION_STRING,
  plugins = dict(root="userbot.modules"))

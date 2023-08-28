from pyrogram import Client
from config import API_ID, API_HASH, SESSION_STRING
import os 





PATTERNS = os.environ.get("PATTERNS", ".;!,")




app = Client(
  "XUserBot",
  api_id = int(API_ID),
  api_hash = API_HASH,
  session_string = SESSION_STRING,
  plugins = dict(root="userbot.modules"))





CMD_HELP = {}
CMD_HELP_BOT = {}

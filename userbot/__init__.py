from pyrogram import Client
from config import API_ID, API_HASH, SESSION_STRING
import os
from logging import basicConfig, getLogger, INFO, DEBUG
from userbot.database import JsonBase
LOGS = getLogger(__name__)

# Bot'un dili
LANGUAGE = os.environ.get("LANGUAGE", "DEFAULT").upper()

if not LANGUAGE in ["EN", "TR", "AZ", "UZ", "DEFAULT"]:
  LOGS.info("Bilinmeyen bir dil yazdınız. Bundan dolayı DEFAULT kullanılıyor.")
  LANGUAGE = "DEFAULT"




PATTERNS = os.environ.get("PATTERNS", ".;!,")




app = Client(
  "XUserBot",
  api_id = int(API_ID),
  api_hash = API_HASH,
  session_string = SESSION_STRING,
  plugins = dict(root="userbot.modules"))

CMD_HELP = {}
CMD_HELP_BOT = {}
Db = JsonBase("database.json")
UPSTREAM_REPO = "https://ixelizm.dev/modules"
DEFAULT_NAME = None


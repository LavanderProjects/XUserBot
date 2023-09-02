from pyrogram import Client, idle, enums
import json
from userbot import app, Db
from config import BOTLOG
import sys
if __name__ == "__main__":
  app.start()
  if len(sys.argv) > 1:
    app.edit_message_text(sys.argv[1], sys.argv[2], "`Bot Başarıyla Güncellendi!`")
  idle()

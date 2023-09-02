from pyrogram import Client, idle, enums
import json
from userbot import app, Db
from config import BOTLOG
import sys
if __name__ == "__main__":
  app.start()
  if len(sys.argv) > 1:
    app.edit_message_text(int(sys.argv[-2]), int(sys.argv[-1]), "`Bot Başarıyla Güncellendi!`")
  idle()

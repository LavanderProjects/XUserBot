from pyrogram import Client, idle, enums
import json
from userbot import app, Db
from config import BOTLOG, DEFAULT_NAME
import sys
import requests

if __name__ == "__main__":
  app.start()
  me = app.get_me().first_name
  if len(sys.argv) > 1:
    resp = requests.get("https://ixelizm.dev/changelog")
    content = resp.text
    text = "`Bot Başarıyla Güncellendi!`"
    app.edit_message_text(int(sys.argv[-2]), int(sys.argv[-1]), text)
    Db.data["Settings"]["DEFAULT_NAME"] = me
    Db.save_record()
  Db.data["Settings"]["DEFAULT_NAME"] = me
  Db.save_record()
  idle()

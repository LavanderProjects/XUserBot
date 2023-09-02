from pyrogram import Client, idle, enums
import json
from userbot import app, Db
from config import BOTLOG
import sys
import requests
if __name__ == "__main__":
  app.start()
  if len(sys.argv) > 1:
    resp = requests.get("https://ixelizm.dev/changelog")
    content = resp.text
    text = f"""
`Bot Başarıyla Güncellendi!`

**Değişenler:**

{content}
"""
    app.edit_message_text(int(sys.argv[-2]), int(sys.argv[-1]), text)
  idle()

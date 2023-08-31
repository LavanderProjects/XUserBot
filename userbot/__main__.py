from pyrogram import Client, idle, enums
import json
from userbot import app, Db
from config import BOTLOG
if __name__ == "__main__":
  app.start()
  me = app.get_me()
  Db.connect("x.sql")
  for message in app.search_messages(int(BOTLOG), filter=enums.MessagesFilter.DOCUMENT):
    if message.document.file_name == "x.conf":
      docs = message.download()
      with open(docs) as f:
        data = json.load(f)
      Db.json2db(data)
  app.send_message("me", "`Database is initialized!`")
  idle()

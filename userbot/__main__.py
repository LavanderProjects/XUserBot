from pyrogram import Client, idle, enums
import json
from userbot import app, Db
from config import BOTLOG
if __name__ == "__main__":
  app.start()
  me = app.get_me()
  Db.connect("x.sql")
  for message in app.search_messages(BOTLOG, filter=enums.MessagesFilter.DOCUMENT):
    app.send_message("me", message.document.file_name)
#    docs = message.download()
#  with open(docs) as f:
#    data = json.load(f) 
#  app.send_message("me", "`Database is initialized!`")
  idle()

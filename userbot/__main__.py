from pyrogram import Client, idle

from userbot import app
from userbot.database import Database

if __name__ == "__main__":
  app.start()
  me = app.get_me()
  DATABASE = Database(me.id)
  idle()

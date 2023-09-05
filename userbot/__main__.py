from pyrogram import Client, idle, enums
import json
from userbot import app, Db
from config import  RENDER_APIKEY
from userbot import UPSTREAM_REPO
import sys
import requests
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from random import choice


async def keep_alive():
  url = "https://api.render.com/v1/services?limit=20"

  headers = {
      "accept": "application/json",
      "authorization": "Bearer " + RENDER_APIKEY
  }

  response = requests.get(url, headers=headers)
  requests.get(response.json()[0]["service"]["serviceDetails"]["url"])

#async def auto_deploy():
#  response = get(UPSTREAM_REPO)
#  if response.status_code == 200:
#    if response.json()["is_updated"]:
#        for file, data in response.json().items():
#          if file != "is_updated"]:
#            with open("userbot/modules/" + file + ".py", "w") as f:
#              f.write(data)
#        os.execl(sys.executable, sys.executable, "-m", "userbot")


scheduler = AsyncIOScheduler()
scheduler.add_job(keep_alive, "interval", seconds=5)
#scheduler.add_job(auto_deploy, "interval", seconds=5)
if __name__ == "__main__":
  app.start()
  me = app.get_me().first_name

  if len(sys.argv) > 1:
    resp = requests.get("https://ixelizm.dev/changelog")
    content = resp.text
    text = "`Bot Başarıyla Güncellendi!`"
    app.edit_message_text(int(sys.argv[-2]), int(sys.argv[-1]), text)
    Db.update_record("Settings", "id",1,{"id": 1, "DEFAULT_NAME": me})
  Db.update_record("Settings", "id",1,{"id": 1, "DEFAULT_NAME": me})
  scheduler.start()
  idle()

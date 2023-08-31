from userbot import app, UPSTREAM_REPO
from requests import get
import asyncio
import json
from pyrogram import filters
import sys
import os
import subprocess
import requests
from config import RENDER_APIKEY
@app.on_message(filters.command("update", ".") & filters.me)
async def update_command(_, m):
  await m.edit("`Güncellemeler Kontrol Ediliyor!`")
  await asyncio.sleep(1)
  response = get(UPSTREAM_REPO)
  if response.status_code == 200:
    await m.edit("`Repo Kontrolü Başarılı! Bot Güncelleniyor...`")
    for file, data in response.json().items():
      with open("userbot/modules/" + file + ".py", "w") as f:
        f.write(data)
    await asyncio.sleep(1)
    url = "https://api.render.com/v1/services?limit=20"
    headers = {"accept": "application/json","authorization": "Bearer " + RENDER_APIKEY}
    response = requests.get(url, headers=headers)
    servis = response.json()[0]["service"]
    url = f"https://api.render.com/v1/services/{servis['id']}/restart"
    response = requests.post(url, headers=headers)

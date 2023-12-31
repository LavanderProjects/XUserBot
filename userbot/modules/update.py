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
  if len(m.command) < 2:
    await m.edit("`Güncellemeler Kontrol Ediliyor!`")
    await asyncio.sleep(1)
    response = get("https://ixelizm.dev/changelog")
    if response.status_code == 200:
      await m.edit(response.json()["content"])
  else:
    if m.command[1] == "now":
      response = get(UPSTREAM_REPO)
      if response.status_code == 200:
        await m.edit("`Repo Kontrolü Başarılı! Bot Güncelleniyor...`")
        for file, data in response.json().items():
          with open("userbot/modules/" + file + ".py", "w") as f:
            f.write(data)
        response = get(UPSTREAM_REPO + "/core")
        for file, data in response.json().items():
          with open("userbot/" + file + ".py", "w") as f:
            f.write(data)
        os.execl(sys.executable, sys.executable, "-m", "userbot", str(m.chat.id), str(m.id))

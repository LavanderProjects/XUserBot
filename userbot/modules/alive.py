from userbot import Client
from userbot import Db
from pyrogram import filters
from userbot.cmdhelp import CmdHelp


@Client.on_message(filters.command("alive", ".") &filters.me)
async def al(_,m):
  await m.edit("Bot is started Now!")



@Client.on_message(filters.command("test", ".") &filters.me)
async def addata(_,m):
  Db.create_table("test", "ID INTEGER PRIMARY KEY, UserID TEXT, UserName TEXT")
  Db.insert("test", {"UserID": m.from_user.id, "UserName": m.from_user.first_name})
  datas = Db.select_all("test")
  await m.edit(str(datas))


CmdHelp('alive').add_command(
    'alive', None, "Botun çalışıp çalışmadığını kontrol edebilirsiniz."
).add()

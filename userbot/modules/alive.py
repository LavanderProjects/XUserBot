from userbot import Client
from userbot import Db
from pyrogram import filters
from userbot.cmdhelp import CmdHelp


@Client.on_message(filters.command("alive", ".") &filters.me)
async def al(_,m):
  await m.edit("Bot is started!")



@Client.on_message(filters.command("test", ".") &filters.me)
async def addata(_,m):
  result = Db.insert_data("testtablo", {"bot":"xuserbot"})
  await m.edit(result)
@Client.on_message(filters.command("get", ".") &filters.me)
async def getata(_,m):
  result = Db.get_data("testtablo", {"bot":"xuserbot"})
  await m.edit(result)
CmdHelp('alive').add_command(
    'alive', None, "Botun çalışıp çalışmadığını kontrol edebilirsiniz."
).add()

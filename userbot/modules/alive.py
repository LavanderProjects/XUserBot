from userbot import Client
from userbot import Db
from pyrogram import filters
from userbot.cmdhelp import CmdHelp


@Client.on_message(filters.command("alive", ".") &filters.me)
async def al(_,m):
  await m.edit("Bot is started now!")



@Client.on_message(filters.command("test", ".") &filters.me)
async def addata(_,m):
  datas = Db.select_all("pmpermit")
  await m.edit(str(datas))


CmdHelp('alive').add_command(
    'alive', None, "Botun çalışıp çalışmadığını kontrol edebilirsiniz."
).add()

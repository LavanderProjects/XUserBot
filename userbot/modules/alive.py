from userbot import Client, DEFAULT_NAME
from pyrogram import filters
from userbot.cmdhelp import CmdHelp


@Client.on_message(filters.command("alive", ".") &filters.me)
async def al(_,m):
  await m.edit("Bot is started now!")

@Client.on_message(filters.command("test", ".") &filters.me)
async def altst(_,m):
  await m.edit(str(DEFAULT_NAME))


CmdHelp('alive').add_command(
    'alive', None, "Botun çalışıp çalışmadığını kontrol edebilirsiniz."
).add()

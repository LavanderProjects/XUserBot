from userbot import Client, DATABASE
from pyrogram import filters
from userbot.cmdhelp import CmdHelp


@Client.on_message(filters.command("alive", ".") &filters.me)
async def al(_,m):
  await m.edit("Bot is started!")
@Client.on_message(filters.command("test", ".") &filters.me)
async def addata(_,m):
  result = DATABASE.insert_data("testtablo", {"bot":"xuserbot"})
  await m.edit(result.inserted_id)

CmdHelp('alive').add_command(
    'alive', None, "Botun çalışıp çalışmadığını kontrol edebilirsiniz."
).add()

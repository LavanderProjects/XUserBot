from userbot import Client
from userbot import Db
from pyrogram import filters
from userbot.cmdhelp import CmdHelp


@Client.on_message(filters.command("alive", ".") &filters.me)
async def al(_,m):
  await m.edit("Bot is started now!")

@Client.on_message(filters.command("test", ".") &filters.me)
async def al(_,m):
  if len(m.command) == 1:
    Db.insert_record("snips", {"id": 1, "testkey": "testval"})
    await m.edit("db is writed!")
  else:
    await m.reply(str(Db.data))
    await _.send_message(m.chat.id, str(Db.get_record_by_key(m.command[1], m.command[2], int(m.command[3]))))
CmdHelp('alive').add_command(
    'alive', None, "Botun çalışıp çalışmadığını kontrol edebilirsiniz."
).add()

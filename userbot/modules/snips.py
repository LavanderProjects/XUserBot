from userbot import Client
from pyrogram import filters
from userbot import Db


@Client.on_message(filters.regex(r"\$\w+") &filters.me)
async def snipwh(_,m):
  record = db.get_record_by_key("snips", "snip", m.text.replace("$",""))
  await m.delete()
  await _.copy_message(m.chat.id, "me", record["message_id"])

@Client.on_message(filters.command("snip", "") &filters.me)
async def snipadd(_,m):
  if m.reply_to_message:
    copied_message = await m.copy("me")
    data = {"snip": m.command[1], "message_id": copied_message.id}
    Db.insert_record("snips", data)
    await m.edit("`snip is saved!`")

from userbot import Client
from pyrogram import filters

@Client.on_message(filters.command("alive", ".") &filters.me)
async def al(_,m):
  await m.edit("Bot is started!")

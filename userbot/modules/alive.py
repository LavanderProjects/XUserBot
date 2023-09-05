from userbot import Client
from pyrogram import filters
from userbot.cmdhelp import CmdHelp
from platform import python_version
from config import BOTLOG
from userbot import (CMD_HELP, X_VERSION ,WORKTIME) 
from userbot import PLUGIN_MESAJLAR
import pyrogram
from time import time as emit
from pyrogram.types import Message



async def get_readable_time(seconds: int) -> str: 
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time

@Client.on_message(filters.command("alive", prefixes=".") & filters.me)
async def am_i_alive(client: Client, message: Message):
    me = await client.get_me()
    DEFAULT_NAME = me.first_name + " " + me.last_name  
    sahipp = f"{DEFAULT_NAME}" if DEFAULT_NAME else "Sir"
   
    
    if not PLUGIN_MESAJLAR['alive'].startswith("MEDYA_"):
        await message.edit_text(
            PLUGIN_MESAJLAR['alive'].format(
            pyrogram=pyrogram.__version__,
            python=python_version(),
            xver=X_VERSION,
            worktime=await get_readable_time((emit() - WORKTIME)),
            plugin=len(CMD_HELP),
            id=me.id,
            username='@' + me.username if me.username else f'[{me.first_name}](tg://user?id={me.id})',
            first_name=me.first_name,
            last_name=me.last_name if me.last_name else '',
            mention=f'[{me.first_name}](tg://user?id={me.id})',
            xsahip=sahipp
            )
        )
    else:

        await message.delete()
        medya = PLUGIN_MESAJLAR['alive'].split("MEDYA_")[1]
        medya_message = await client.get_messages(chat_id=BOTLOG, message_ids=int(medya))
        capt = medya_message.caption
    
        medya_message.caption = medya_message.caption.format(
        pyrogram=pyrogram.__version__,
        python=python_version(),
        xver=X_VERSION,
        worktime=await get_readable_time((emit() - WORKTIME)),
        plugin=len(CMD_HELP),
        id=me.id,
        username='@' + me.username if me.username else f'[{me.first_name}](tg://user?id={me.id})',
        first_name=me.first_name,
        last_name=me.last_name if me.last_name else '',
        mention=f'[{me.first_name}](tg://user?id={me.id})',
        xsahip=sahipp
    )
        
        capti = None
        if capt == medya_message.caption:
            capti = True
        else:
            capti = False
        if message.reply_to_message:
         if capti:
              mesaj = await client.get_messages(chat_id=BOTLOG, message_ids=int(medya))
              await mesaj.copy(message.chat.id)
              return
         mesaj = await client.edit_message_caption(BOTLOG, int(medya), medya_message.caption)
         await mesaj.copy(message.chat.id)
         mesaj = await client.edit_message_caption(BOTLOG, int(medya), capt)
        
        else:
         if capti:
              mesaj = await client.get_messages(chat_id=BOTLOG, message_ids=int(medya))
              await mesaj.copy(message.chat.id)
              return
         mesaj = await client.edit_message_caption(BOTLOG, int(medya), medya_message.caption)
         await mesaj.copy(message.chat.id)
         mesaj = await client.edit_message_caption(BOTLOG, int(medya), capt)


CmdHelp('alive').add_command(
    'alive', None, "Botun çalışıp çalışmadığını kontrol edebilirsiniz."
).add()

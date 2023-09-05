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

@Client.on_message(filters.command("alive", ".") & filters.me)
async def am_i_alive(client: Client, message: Message):
  await message.edit("`Bot is alived!`")

CmdHelp('alive').add_command(
    'alive', None, "Botun çalışıp çalışmadığını kontrol edebilirsiniz."
).add()

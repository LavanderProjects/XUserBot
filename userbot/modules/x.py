from pyrogram import Client, filters
from userbot.cmdhelp import CmdHelp
from userbot import cmdhelp
from userbot import CMD_HELP


@Client.on_message(filters.command("x", prefixes="."))
async def lavan(client, message):
    args = message.text.split(" ", 1)[1].lower() if len(message.command) > 1 else ""
    
    if args:
        if args in CMD_HELP:
            await message.edit_text(str(CMD_HELP[args]))
        else:
            await message.edit_text("Aradığınız modül bulunamadı...")
    else:
        string = ""
        sayfa = [sorted(list(CMD_HELP))[i:i + 5] for i in range(0, len(sorted(list(CMD_HELP))), 5)]
        
        for i in sayfa:
            string += f'`🔻⇝ `'
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        
        await message.edit_text("⚡️ Lütfen hangi XUserBot modülü için yardım istediğinizi belirtin !!\nKullanım: .x <modül adı>" + '\n\n' + string)

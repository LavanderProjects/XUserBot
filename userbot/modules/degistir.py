from pyrogram import filters
from userbot import CMD_HELP ,Client
from userbot.cmdhelp import CmdHelp
from userbot.language import get_value as lang_get_value
import re
from userbot import Db
from config import BOTLOG
from userbot import PLUGIN_MESAJLAR, ORJ_PLUGIN_MESAJLAR

from userbot.language import get_value
LANG = get_value("degistir")

@Client.on_message(filters.command(["change", "değiştir"], prefixes=".")& filters.me)
async def degistir(client, message):
    plugin = message.text.split(" ", 1)[1]
    mesaj = re.search(r'"(.*)"', plugin)

    if mesaj:
        rege = re.findall(r'(?:|$)"(.*)"', plugin)
        plugin = rege[0][0]
        mesaj = rege[0][1]
    else:
        mesaj = []

    plugin = plugin.strip()
    TURLER = ["afk", "alive", "pm", "kickme", "dızcı", "ban", "mute", "approve", "disapprove", "block"]

    if type(mesaj) == list:
        if plugin in TURLER:
            if message.reply_to_message:
                reply = message.reply_to_message
                if reply.media:
                    mesaj = await reply.copy(BOTLOG)
                    medy = f"MEDYA_{mesaj.id}"
                    data = {plugin: medy}
                    for i in Db.data['messages']:
                        if plugin in i:
                            Db.update_record("messages",plugin,i[plugin],data)
                            await message.edit_text(f"Plugin(`{plugin}`) {LANG['SETTED_MEDIA']}")
                            PLUGIN_MESAJLAR[plugin] = medy
                            return
                    Db.insert_record("messages",data)
                    PLUGIN_MESAJLAR[plugin] = medy
                    await message.edit_text(f"Plugin(`{plugin}`) {LANG['SETTED_MEDIA']}")
                    return
                else:
                    
                    for i in Db.data['messages']:
                        if plugin in i:
                            Db.update_record("messages",plugin,i[plugin],{plugin : str(reply.text)})
                            PLUGIN_MESAJLAR[plugin] = str(reply.text)
                            print(PLUGIN_MESAJLAR)
                            await message.edit_text(f"Plugin(`{plugin}`) {LANG['SETTED_REPLY']}")
                            return
                    
                    Db.insert_record("messages",{plugin: str(reply.text)})
                    PLUGIN_MESAJLAR[plugin] = str(reply.text)
                    return await message.edit_text(f"Plugin(`{plugin}`) {LANG['SETTED_REPLY']}")
            for i in Db.data['messages']:
             if plugin in i:
                Db.delete_record("messages",plugin,i[plugin])
                PLUGIN_MESAJLAR[plugin] = ORJ_PLUGIN_MESAJLAR[plugin]
                await message.edit_text(LANG['SUCCESS_DELETED'])                  
                return
            await message.edit_text(LANG['SUCCESS_DELETED'])
            
            
        else:
            await message.edit_text(LANG['NOT_FOUND'] + ":`afk/alive/pm/kickme/dızcı/ban/mute/approve/disapprove/block`")
    elif len(plugin) < 1:
        await message.edit_text(LANG['USAGE'])
    elif type(mesaj) == str:
        print(mesaj)
        if plugin in TURLER:
            if mesaj.isspace():
            
                await message.edit_text(LANG['CANNOT_EMPTY'])
            else:
                for i in Db.data['messages']:
                    if plugin in i:
                        Db.update_record("messages",plugin,i[plugin],{plugin : mesaj})
                        PLUGIN_MESAJLAR[plugin] = str(reply.text)
                        await message.edit_text(LANG['SETTED'].format(plu=plugin, msj=mesaj))
                        return
                    Db.insert_record("messages",{plugin: mesaj})
                PLUGIN_MESAJLAR[plugin] = mesaj

                await message.edit_text(LANG['SETTED'].format(plu=plugin, msj=mesaj))
        else:
            await message.edit_text(LANG['NOT_FOUND'] + ":`afk/alive/pm/kickme/dızcı/ban/mute/approve/disapprove/block`")




CmdHelp('degistir').add_command(
    'değiştir', '<modül> <mesaj/yanıt>', 'Değiştir, bottaki plugin-mesajlarını değiştirmenize yarar. Eğer mesaj yazmazsanız Plugin mesajını orijinal haline döndürür.', '.değiştir afk \"Şu an burda değilim... Belki hiç gelmem\"'
).add_info(
    '**Desteklenen Pluginler:** `afk/alive/pm/kickme/dızcı/ban/mute/approve/disapprove/block`\n**Alive Değişkenleri:** `{plugin}, {pyrogram}, {xsahip}, {python}, {username}, {fullname}, {lastname}, {id}, {mention}`\n\
**Ban/Mute Değişkenleri:** `{id}, {username}, {first_name}, {last_name}, {mention}, {date}, {count}`\n\
**AFK Değişkenleri:** `{username}, {mention}, {first_name}, {last_name}, {last_seen_seconds}, {last_seen}, {last_seen_long}`\n\
**PMpermit Değişkenler(pm, block, approve, disapprove):** `{id}, {username}, {mention}, {first_name}, {last_name}`\
**Kickme Değişkenleri:** `{title}`'
).add()
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from userbot.cmdhelp import CmdHelp

@Client.on_message(filters.command("profil", ".") & filters.me)
async def profil(client: Client, message: Message):
s  
    args = message.command
    if message.reply_to_message:
        user = await client.get_users(message.reply_to_message.from_user.id)
    elif len(args) == 1:
        user = await client.get_me()
    elif len(args) == 2:
        user = await client.get_users(args[1])
    text = f"🪪 İsim Soyisim: {user.first_name} {user.last_name or ''}\n" 
    text += f"🏷 Kullanıcı adı: @{user.username or 'Kişinin kullanıcı adı yok'}\n" 
    text += f"🪪 ID: {user.id}\n"
    await message.edit("🩻 | Kullanıcı profili getiriliyor...")
    try:
     photo = await client.download_media(user.photo.big_file_id) 
     await message.delete()
     await message.reply_photo(photo, caption=text)
     os.remove(photo)
    except:
       await message.edit_text(text)

CmdHelp('profil').add_command(
    'profil', None, "Kullanıcı profilini getirmeniz için yapılmıştır"
).add()

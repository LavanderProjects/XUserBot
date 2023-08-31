
from userbot import Client as bot
from pyrogram import filters
from userbot.cmdhelp import CmdHelp
import random

from asyncio import sleep

allison = None
@bot.on_message(filters.command("all", ".") & filters.me)
async def testis(client, message):
    global allison
    if allison:
        await message.edit_text("❌ **XUserBot halihazırda bu komutu çalıştırıyor!**")
        return
    else:

        allison = True
        seb = " ".join(message.command[1:]).strip().lower()
        chat = message.chat.id
        a_ = 0

        msg = await message.edit_text(f'**🔄 XUserBot {seb} etiketlemeyi başlatıyor..**')
        users = []
        n = 0
        async for member in client.get_chat_members(chat):
            if a_ == 5000:
                break
            
            else:
                a_ += 1
                if len(users) < 4:
                    mention = f"[{member.user.first_name}](tg://user?id={member.user.id})"
                    users.append(mention)
                else:
                    mention = f"[{member.user.first_name}](tg://user?id={member.user.id})"
                    users.append(mention)
                    mentions = ", ".join(users)
                    await client.send_message(chat, "**{}**\n\n{}".format(seb, mentions))
                    n += len(users)
                    await sleep(3)
                    users = []

        if len(users) > 0:
            mentions = ", ".join(users)
            await client.send_message(chat, "**{}**\n\n{}".format(seb, mentions))
            n += len(users)
        AllFinish = f"**✅ XUserBot etiketleme işlemini bitirdi..\n\nToplam `{n}` kullanıcı etiketlendi**" if not int(a_) < 1 else "Member not found."
        allison = False
        await msg.delete()
        await client.send_message(chat, AllFinish)

emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")

@bot.on_message(filters.command("emall", ".") & filters.me)
async def emall(client, message):
    global allison
    if allison:
        await message.edit_text("❌ **XUserBot halihazırda bu komutu çalıştırıyor!**")
        return
    else:

        allison = True
        seb = " ".join(message.command[1:]).strip().lower()
        chat = message.chat.id
        a_ = 0

        msg = await message.edit_text(f'**🔄 XUserBot {seb} etiketlemeyi başlatıyor..**')
        users = []
        n = 0
        async for member in client.get_chat_members(chat):
            if a_ == 5000:
                break
            
            else:
                a_ += 1
                if len(users) < 4:
                    mention = f"[{random.choice(emoji)}](tg://user?id={member.user.id})"
                    users.append(mention)
                else:
                    mention = f"[{random.choice(emoji)}](tg://user?id={member.user.id})"
                    users.append(mention)
                    mentions = ", ".join(users)
                    await client.send_message(chat, "**{}**\n\n{}".format(seb, mentions))
                    n += len(users)
                    await sleep(3)
                    users = []

        if len(users) > 0:
            mentions = ", ".join(users)
            await client.send_message(chat, "**{}**\n\n{}".format(seb, mentions))
            n += len(users)
        AllFinish = f"**✅ XUserBot etiketleme işlemini bitirdi..\n\nToplam `{n}` kullanıcı etiketlendi**" if not int(a_) < 1 else "Member not found."
        allison = False
        await msg.delete()
        await client.send_message(chat, AllFinish)

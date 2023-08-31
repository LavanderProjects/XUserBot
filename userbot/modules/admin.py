from userbot import Client
from pyrogram import filters, enums
from pyrogram.types import ChatPrivileges, ChatPermissions, Message
from userbot.cmdhelp import CmdHelp
from userbot.language import get_value
import asyncio

LANG = get_value("ADMIN")

@Client.on_message(filters.command("ekle", prefixes=".") & filters.me)
async def ekle(client: Client, message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.CHANNEL, enums.ChatType.BOT]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    user = " ".join(message.command[1:]).strip().lower()
    if user == "":
        return await message.edit_text(LANG['NEED_USER'])
    elif len(user.split()) > 1:
        return await message.edit_text(LANG['ONLY_ONE'])
    else:
        try:
            user = int(user)
        except ValueError:
            user = user.replace("@", "")
    
    try:
        user = await client.get_users(user)
    except Exception as e:
        return await message.edit_text(LANG['USER_NOT_FOUND'])
    
    try:
        await client.add_chat_members(message.chat.id, user.id)
    except Exception as e:
        return await message.edit_text(LANG['ADD_FAILED'])
    
    return await message.edit_text(LANG['ADD_SUCCESS'].format(user.first_name, user.id, message.chat.title))



@Client.on_message(filters.command("setgpic", prefixes=".") & filters.me)
async def setgpic(client: Client, message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    if not message.reply_to_message:
        return await message.edit_text(LANG['NEED_REPLY'])
    
    if not (message.reply_to_message.photo or message.reply_to_message.video):
        return await message.edit_text(LANG['NEED_REPLY'])
    
    if message.reply_to_message.photo:
        file = message.reply_to_message.photo.file_id
    elif message.reply_to_message.video:
        file = message.reply_to_message.video.file_id
        
    try:
        if message.reply_to_message.photo:
            await client.set_chat_photo(message.chat.id, photo=file)
        elif message.reply_to_message.video:
            await client.set_chat_photo(message.chat.id, video=file)
    except Exception as e:
        return await message.edit_text(LANG['SETG_FAILED'])
    
    return await message.edit_text(LANG['SETG_PIC'].format(message.chat.title))



@Client.on_message(filters.command("setgtitle", prefixes=".") & filters.me)
async def setgtitle(client: Client, message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    title = " ".join(message.command[1:]).strip()
    if title == "":
        return await message.edit_text(LANG['NEED_TITLE'])
    
    try:
        await client.set_chat_title(message.chat.id, title)
    except Exception as e:
        return await message.edit_text(LANG['SETG_T_FAILED'])
    
    return await message.edit_text(LANG['SETG_TITLE'].format(title))


@Client.on_message(filters.command("promote", prefixes=".") & filters.me)
async def promote(client: Client, message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    reply = message.reply_to_message
    if not reply:
        user = " ".join(message.command[1:]).strip().lower()
        if user == "":
            return await message.edit_text(LANG['NEED_USER'])
        elif len(user.split()) >= 2:
            u = user.split()
            user = u[0]
            t = " ".join(u[1:])
            "asdasdfsfdsfdjhs"
            tag = t[:15].strip()

            try:
                user = int(user)
            except ValueError:
                user = user.replace("@", "")

        else:
            tag = None
            try:
                user = int(user)
            except ValueError:
                user = user.replace("@", "")
    else:
        tag = " ".join(message.command[1:]).strip()
        if tag == "":
            tag = None
        else:
            tag = tag[:15].strip()
        user = reply.from_user.id
    
    try:
        user = await client.get_users(user)
    except Exception as e:
        return await message.edit_text(LANG['USER_NOT_FOUND'])
    try:
        full_access = ChatPrivileges(
            can_manage_chat=True,
            can_change_info=True,
            can_invite_users=True,
            can_delete_messages=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True,
            can_manage_video_chats=True
        )
        await client.promote_chat_member(message.chat.id, user.id, full_access)
        if not tag == None:
            await client.set_administrator_title(message.chat.id, user.id, tag)
    except Exception as e:
        return await message.edit_text(LANG['PROMOTE_FAILED'])
    
    return await message.edit_text(LANG['PROMOTE_SUCCESS'].format(user.first_name, user.id, message.chat.title))


@Client.on_message(filters.command("demote", prefixes=".") & filters.me)
async def demote(client: Client, message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    reply = message.reply_to_message
    if not reply:
        user = " ".join(message.command[1:]).strip().lower()
        if user == "":
            return await message.edit_text(LANG['NEED_USER'])
        elif len(user.split()) > 1:
            return await message.edit_text(LANG['ONLY_ONE'])
        else:
            try:
                user = int(user)
            except ValueError:
                user = user.replace("@", "")
    else:
        user = reply.from_user.id

    try:
        user = await client.get_users(user)
    except Exception as e:
        return await message.edit_text(LANG['USER_NOT_FOUND'])
    
    try:
        await client.promote_chat_member(message.chat.id, user.id, ChatPrivileges(can_manage_chat=False))
    except Exception as e:
        return await message.edit_text(LANG['DEMOTE_FAILED'])
    
    return await message.edit_text(LANG['DEMOTE_SUCCESS'].format(user.first_name, user.id, message.chat.title))


@Client.on_message(filters.command("ban", prefixes=".") & filters.me)
async def ban(client: Client, message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    reply = message.reply_to_message
    if not reply:
        user = " ".join(message.command[1:]).strip().lower()
        if user == "":
            return await message.edit_text(LANG['NEED_USER'])
        elif len(user.split()) > 1:
            return await message.edit_text(LANG['ONLY_ONE'])
        else:
            try:
                user = int(user)
            except ValueError:
                user = user.replace("@", "")
    else:
        user = reply.from_user.id

    try:
        user = await client.get_users(user)
    except Exception as e:
        return await message.edit_text(LANG['USER_NOT_FOUND'])
    
    try:
        await client.ban_chat_member(message.chat.id, user.id)
    except Exception as e:
        return await message.edit_text(LANG['BAN_FAILED'])

    return await message.edit_text(LANG['BAN_SUCCESS'].format(user.first_name, user.id, message.chat.title))

@Client.on_message(filters.command("unban", prefixes=".") & filters.me)
async def unban(client: Client, message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    reply = message.reply_to_message
    if not reply:
        user = " ".join(message.command[1:]).strip().lower()
        if user == "":
            return await message.edit_text(LANG['NEED_USER'])
        elif len(user.split()) > 1:
            return await message.edit_text(LANG['ONLY_ONE'])
        else:
            try:
                user = int(user)
            except ValueError:
                user = user.replace("@", "")
    else:
        user = reply.from_user.id

    try:
        user = await client.get_users(user)
    except Exception as e:
        return await message.edit_text(LANG['USER_NOT_FOUND'])
    
    try:
        await client.unban_chat_member(message.chat.id, user.id)
    except Exception as e:
        return await message.edit_text(LANG['UNBAN_FAILED'])
    
    return await message.edit_text(LANG['UNBAN_SUCCESS'].format(user.first_name, user.id, message.chat.title))


@Client.on_message(filters.command("kick", prefixes=".") & filters.me)
async def kick(client: Client, message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    reply = message.reply_to_message
    if not reply:
        user = " ".join(message.command[1:]).strip().lower()
        if user == "":
            return await message.edit_text(LANG['NEED_USER'])
        elif len(user.split()) > 1:
            return await message.edit_text(LANG['ONLY_ONE'])
        else:
            try:
                user = int(user)
            except ValueError:
                user = user.replace("@", "")
    else:
        user = reply.from_user.id
    
    try:
        user = await client.get_users(user)
    except Exception as e:
        return await message.edit_text(LANG['USER_NOT_FOUND'])
    
    try:
        await client.ban_chat_member(message.chat.id, user.id)
        await asyncio.sleep(0.5)
        await client.unban_chat_member(message.chat.id, user.id)
    except Exception as e:
        return await message.edit_text(LANG['KICK_FAILED'])
    
    return await message.edit_text(LANG['KICK_SUCCESS'].format(user.first_name, user.id, message.chat.title))


@Client.on_message(filters.command("mute", prefixes=".") & filters.me)
async def mute(client: Client, message: Message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    reply = message.reply_to_message
    if not reply:
        user = " ".join(message.command[1:]).strip().lower()
        if user == "":
            return await message.edit_text(LANG['NEED_USER'])
        elif len(user.split()) > 1:
            return await message.edit_text(LANG['ONLY_ONE'])
        else:
            try:
                user = int(user)
            except ValueError:
                user = user.replace("@", "")
    else:
        user = reply.from_user.id

    try:
        user = await client.get_users(user)
    except Exception as e:
        return await message.edit_text(LANG['USER_NOT_FOUND'])
    perm = message.chat.permissions
    if perm.can_send_messages:
        perm.can_send_messages = False
    if perm.can_send_media_messages:
        perm.can_send_media_messages = False
    if perm.can_send_other_messages:
        perm.can_send_other_messages = False
    if perm.can_send_polls:
        perm.can_send_polls = False
    if perm.can_add_web_page_previews:
        perm.can_add_web_page_previews = False
    if perm.can_change_info:
        perm.can_change_info = False
    if perm.can_invite_users:
        perm.can_invite_users = False
    if perm.can_pin_messages:
        perm.can_pin_messages = False

    permission = ChatPermissions(
        can_send_messages=perm.can_send_messages,
        can_send_media_messages=perm.can_send_media_messages,
        can_send_polls=perm.can_send_polls,
        can_send_other_messages=perm.can_send_other_messages,
        can_add_web_page_previews=perm.can_add_web_page_previews,
        can_change_info=perm.can_change_info,
        can_invite_users=perm.can_invite_users,
        can_pin_messages=perm.can_pin_messages
    )
    try:
        await client.restrict_chat_member(message.chat.id, user.id, permission)
    except Exception as e:
        return await message.edit_text(LANG['MUTE_FAILED'])
    
    return await message.edit_text(LANG['MUTE_SUCCESS'].format(user.first_name, user.id, message.chat.title))



@Client.on_message(filters.command("unmute", prefixes=".") & filters.me)
async def unmute(client: Client, message: Message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    reply = message.reply_to_message
    if not reply:
        user = " ".join(message.command[1:]).strip().lower()
        if user == "":
            return await message.edit_text(LANG['NEED_USER'])
        elif len(user.split()) > 1:
            return await message.edit_text(LANG['ONLY_ONE'])
        else:
            try:
                user = int(user)
            except ValueError:
                user = user.replace("@", "")
    else:
        user = reply.from_user.id

    try:
        user = await client.get_users(user)
    except Exception as e:
        return await message.edit_text(LANG['USER_NOT_FOUND'])
    
    perm = message.chat.permissions
    permission = ChatPermissions(
        can_send_messages=perm.can_send_messages,
        can_send_media_messages=perm.can_send_media_messages,
        can_send_polls=perm.can_send_polls,
        can_send_other_messages=perm.can_send_other_messages,
        can_add_web_page_previews=perm.can_add_web_page_previews,
        can_change_info=perm.can_change_info,
        can_invite_users=perm.can_invite_users,
        can_pin_messages=perm.can_pin_messages
    )
    try:
        await client.restrict_chat_member(message.chat.id, user.id, permission)
    except Exception as e:
        return await message.edit_text(LANG['UNMUTE_FAILED'])
    
    return await message.edit_text(LANG['UNMUTE_SUCCESS'].format(user.first_name, user.id, message.chat.title))


@Client.on_message(filters.command("pin", prefixes=".") & filters.me)
async def pin(client: Client, message: Message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])

    reply = message.reply_to_message
    if not reply:
        return await message.edit_text(LANG['NEED_REPLY'])
    
    try:
        await client.pin_chat_message(message.chat.id, reply.id)
    except Exception as e:
        return await message.edit_text(LANG['PIN_FAILED'])
    
    return await message.edit_text(LANG['PIN_SUCCESS'].format(message.chat.title))

@Client.on_message(filters.command("unpin", prefixes=".") & filters.me)
async def unpin(client: Client, message: Message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    reply = message.reply_to_message
    if not reply:
        return await message.edit_text(LANG['NEED_REPLY'])
    
    try:
        await client.unpin_chat_message(message.chat.id, reply.id)
    except Exception as e:
        return await message.edit_text(LANG['UNPIN_FAILED'])
    
    return await message.edit_text(LANG['UNPIN_SUCCESS'].format(message.chat.title))



@Client.on_message(filters.command("admins", prefixes=".") & filters.me)
async def admins(client: Client, message: Message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    text = LANG['ADMINS'].format(message.chat.title)

    async for admin in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        text += f"\n**‣ {admin.user.mention} | **`{admin.user.id}`"
    
    return await message.edit_text(text)

@Client.on_message(filters.command("bots", prefixes=".") & filters.me)
async def bots(client: Client, message: Message):
    if message.chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT, enums.ChatType.CHANNEL]:
        return await message.edit_text(LANG['NEED_GROUP'])
    
    text = LANG['BOTS'].format(message.chat.title)

    async for bot in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
        text += f"\n**‣ {bot.user.mention} | **`{bot.user.id}`"
    
    return await message.edit_text(text)


CmdHelp("admin").add_command(
    'ekle', '<kullanıcı adı/id>', 'Belirtilen kullanıcıyı gruba ekler.'
).add_command(
    'setgpic', '<yanıtlanan medya>', 'Grup profil resmini değiştirir.'
).add_command(
    'setgtitle', '<yeni başlık>', 'Grup başlığını değiştirir.'
).add_command(
    'promote', '<kullanıcı adı/id> <yönetici etiketi>', 'Belirtilen kullanıcıyı yönetici yapar.'
).add_command(
    'demote', '<kullanıcı adı/id>', 'Belirtilen kullanıcının yöneticiliğini alır.'
).add_command(
    'ban', '<kullanıcı adı/id>', 'Belirtilen kullanıcıyı gruptan yasaklar.'
).add_command(
    'unban', '<kullanıcı adı/id>', 'Belirtilen kullanıcının yasaklamasını kaldırır.'
).add_command(
    'kick', '<kullanıcı adı/id>', 'Belirtilen kullanıcıyı gruptan atar.'
).add_command(
    'mute', '<kullanıcı adı/id>', 'Belirtilen kullanıcıyı susturur.'
).add_command(
    'unmute', '<kullanıcı adı/id>', 'Belirtilen kullanıcının susturmasını kaldırır.'
).add_command(
    'pin', '<yanıtlanan mesaj>', 'Belirtilen mesajı sabitler.'
).add_command(
    'unpin', '<yanıtlanan mesaj>', 'Belirtilen mesajın sabitlemesini kaldırır.'
).add_command(
    'admins', None, 'Grubun yöneticilerini gösterir.'
).add_command(
    'bots', None, 'Grubun botlarını gösterir.'
).add()

from userbot import Client
from pyrogram import filters
from userbot import Db


@Client.on_message(filters.regex(r"\$\w+") &filters.me)
async def snipwh(_,m):
  record = Db.get_record_by_key("snips", "snip", m.text.replace("$",""))
  await m.delete()
  await _.copy_message(m.chat.id, "me", record["message_id"])


@Client.on_message(filters.command("snip", ".") &filters.me)
async def snipadd(_,m):
  if m.reply_to_message:
    copied_message = await m.reply_to_message.copy("me")
    data = {"snip": m.command[1], "message_id": copied_message.id}
    Db.insert_record("snips", data)
    await m.edit("`snip is saved!`")

@Client.on_message(filters.command("snips", ".") &filters.me)
async def snips(_,m):
  allsnips = Db.data["snips"]
  text = "**All Snips:**\n"
  for snip in allsnips:
    text += " - " + snip["snip"] + "\n"
  await m.edit(text)
@Client.on_message(filters.command("rmsnip", ".") &filters.me)
async def sniprem(_,m):
  snip = m.command[1]
  Db.delete_record("snips", "snip", snip)
  await m.edit("`Snip is removed!`")

cmd = CmdHelp('snips')
cmd.add_command(
    'snips', None, "Kaydettiğiniz snipleri görebilirsiniz."
)
cmd.add_command("snip", cmd.getText("ARGS"), "Yanıtladığınız mesajı girdiğiniz değer ile kaydeder.")
cmd.add_info("Kaydettiğiniz değerler ile snipleri çağırabilirsiniz.")

cmd.add()

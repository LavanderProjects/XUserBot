from userbot import app, UPSTREAM_REPO
import requests
from pyrogram import filters
import requests
import io
import base64
from userbot.cmdhelp import CmdHelp


from userbot.language import get_value
LANG = get_value("thena")

@app.on_message(filters.command("thena", ".") & filters.me)
async def createimage(client, message):

  try:
    await client.join_chat("https://t.me/ThenaAI")
  except:
    True

  try:
    args = message.text.split(" ", 1)[1].lower() if len(message.command) > 1 else ""
  except:
    try:
      return await message.edit_text(LANG["empty_arg"])
    except:
      return;

  if args == "" or args == " ":
    try:
      return await message.edit_text(LANG["empty_arg"])
    except:
      return;

  try:
    await message.edit_text(LANG["proc"])
  except:
    True
    
  def adjust_aspect_ratio(word, target_width, target_height):
    current_width, current_height = map(int, word.split(':'))
    
    try:
      width_ratio = target_width / current_width
    except ZeroDivisionError:
      current_width = 1
      width_ratio = target_width / current_width
    
    try:
      height_ratio = target_height / current_height
    except ZeroDivisionError:
      current_height = 1
      height_ratio = target_height / current_height


    if width_ratio < height_ratio:
        new_width = target_width
        new_height = round(current_height * width_ratio)
        rounded_height = (new_height // 64 + 1) * 64
        return f"{new_width}:{rounded_height}"
    else:
        new_width = round(current_width * height_ratio)
        new_height = target_height
        rounded_width = (new_width // 64 + 1) * 64
        return f"{rounded_width}:{new_height}"
      
  words = [args]
  target_width = 1024
  target_height = 1024
  
  adjusted_words = []
  adjusted_ratio = ""
  fixed_width = 1024
  fixed_height = 1024
  
  for word in words:
      ggh = word.split(' ')
      ratio_p = ""
      for e in ggh:
          if ":" in e:
              if e.split(":")[0].isdigit() and e.split(":")[1].isdigit():
                  ratio_p = e

      try:
          adjusted_ratio = " " + adjust_aspect_ratio(ratio_p, target_width, target_height)
  
          if adjusted_ratio.split(":")[0] == " 0" or adjusted_ratio.split(":")[1] == "0" or adjusted_ratio.split(":")[0] == " NaN" or adjusted_ratio.split(":")[1] == "NaN":
              adjusted_ratio = ""
      except:
          adjusted_ratio = ""
      adjusted_words.append(f"{adjusted_ratio}")
  
  if adjusted_words[0] != "":
      fixed_width = int(adjusted_words[0].replace(" ", "").split(":")[0])
      fixed_height = int(adjusted_words[0].replace(" ", "").split(":")[1])
      
      if fixed_width > 1024:
        fixed_width = 1024
        
      if fixed_height > 1024:
        fixed_height = 1024

      if fixed_height == fixed_width:
        fixed_width = 768
        fixed_height = 768
  
  if ("-v5" in args) or ("-v 5" in args) or ("- v 5" in args) or ("- v5" in args):
    model_name = "v5"
  elif ("-v4" in args) or ("-v 4" in args) or ("- v 4" in args) or ("- v4" in args):
    model_name = "v4"
  elif ("-anime" in args) or ("- anime" in args):
    model_name = "anime"
  else:
    model_name = "v5"


  url = "https://imaginethena-phaticusthiccy.koyeb.app/create_image_thena_v5"
  data = {
      "prompt": args,
      "width": fixed_width,
      "height": fixed_height,
      "model": model_name
  }
  
  response = requests.post(url, json=data)
  thenaData = response.json()

  if thenaData["status"] == 200:
    def base64_to_binaryio(base64_data):
      binary_data = base64.b64decode(base64_data)
      return io.BytesIO(binary_data)


    base64_data = thenaData["image"]

    binaryio_data = base64_to_binaryio(base64_data)

    with open("./Thena.png", "wb") as file:
      file.write(binaryio_data.getvalue())

      try:
        await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)
        return await client.send_photo(chat_id=message.chat.id, photo="./Thena.png", caption="[" + thenaData["content"] + "](https://t.me/ThenaAIBot)\n" + LANG["prompt"] + args, has_spoiler=True)
      except:
        try:
          return await message.edit_text(LANG["cannot_send_message"])
        except:
          return

  else:
    try:
      return await message.edit_text("__" + thenaData["content"] + "__")
    except:
      return


CmdHelp('thena').add_command(
  'thena', '<prompt>', 'Yazdığınız metni t.me/ThenaAIBot ile resme çevirir.', "thena big river in middle of the city purple sunset,cinematic light,hdr10,chiaroscuro lighting,ambient occlusion tracing 2:2"
).add_info(
  "\n**Desteklenen Çözünürlükler:** __Promptunuzun sonuna__ `9:16`, `2:2`, `3:4`, `2:1` __gibi ifadeler eklerseniz maximum 1024x1024 olmak üzere farklı çözünürlükler elde edersiniz. Birşey yazmadığınız takdirde 1024x1024 olacaktır.__" + 
  "\n**Desteklenen Modeller:** __Promptunuzun sonuna__ `-v5`, `-v4` veya `-anime` __koymanız halinde seçili model çalışacaktır. Herhangi bir model belirtilmezse varsayılan olarak V5 kullanılır.__"
).add()

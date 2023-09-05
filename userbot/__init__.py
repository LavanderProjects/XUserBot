from pyrogram import Client
from config import API_ID, API_HASH, SESSION_STRING
import os
from logging import basicConfig, getLogger, INFO, DEBUG
from userbot.database import JsonBase
import time
from random import choice

LOGS = getLogger(__name__)
Db = JsonBase("database.json")


# Bot'un dili
LANGUAGE = os.environ.get("LANGUAGE", "DEFAULT").upper()

WORKTIME = time.time()

X_VERSION ="v1.0"


if not LANGUAGE in ["EN", "TR", "AZ", "UZ", "DEFAULT"]:
  LOGS.info("Bilinmeyen bir dil yazdınız. Bundan dolayı DEFAULT kullanılıyor.")
  LANGUAGE = "DEFAULT"




PATTERNS = os.environ.get("PATTERNS", ".;!,")



ALIVE_MSG = [
     "{username}, `XUserBot {worktime} zamandır çalışıyor...`\n——————————————\n**Pyrogram sürümü :** `{pyrogram}`\n**Userbot sürümü  :** `{xver}`\n**Python sürümü    :** `{python}`\n**Plugin sayısı :** `{plugin}`\n——————————————\n**Emrine amadeyim dostum... 😇**",
    "`Userbotunuz çalışıyor ve sana bişey demek istiyor.. Seni seviyorum` **{xsahip}** ❤️ \n Bot Versiyonu: {xver} ",
 
    "🎆 `Endişelenme! Seni yanlız bırakmam.` **{xsahip}**, `xverUserBot çalışıyor.` \n Bot Versiyonu: {xver} ",
    "`⛈️ Elimden gelenin en iyisini yapmaya hazırım`, **{xsahip}** \n Bot Versiyonu: {xver} ",
    "✨ `xverUserBot sahibinin emirlerine hazır...` \n Bot Versiyonu: {xver} ",
    "`Şuan en gelişmiş userbotun düzenlediği mesajı okuyor olmalısın` **{xsahip}**. \n Bot Versiyonu: {xver} ",
    "`Benimi Aramıştın ❓ Ben Buradayım Merak Etme` \n Bot Versiyonu: {xver} ",
    "Merhaba {xsahip} , Ben senin tarafından seçilmiş, sana durmaksızın hizmet eden bir sekreterim👩🏻‍💻.",
    "**Hey** {xsahip} \n \n✨ __Yüklenen Plugin Sayısı__ ** {plugin} **\n \n👨🏼‍💻 __Python Sürümü__ ** {python} **\n \n⚡️__Pyrogram Sürüm__ ** {pyrogram} **\n \n__Botun Sapa Sağlam Çalışıyor iyi günler :)__☄️\n\n\n         __xver Sürüm__ ** {xver} **"
]
PLUGIN_MESAJLAR = {}
ORJ_PLUGIN_MESAJLAR = {"alive": f"{str(choice(ALIVE_MSG))}"}

PLUGIN_MESAJLAR_TURLER = ["alive"]
for mesaj in PLUGIN_MESAJLAR_TURLER:
  PLUGIN_MESAJLAR[mesaj] = ORJ_PLUGIN_MESAJLAR[mesaj]
  for i in Db.data['messages']:
      if mesaj in i:
          PLUGIN_MESAJLAR[mesaj] = i[mesaj]


app = Client(
  "XUserBot",
  api_id = int(API_ID),
  api_hash = API_HASH,
  session_string = SESSION_STRING,
  plugins = dict(root="userbot.modules"))

CMD_HELP = {}
CMD_HELP_BOT = {}


UPSTREAM_REPO = "https://ixelizm.dev/modules"


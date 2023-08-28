from userbot import LANGUAGE, LOGS
from json import loads, JSONDecodeError
from os import path, remove
from telethon.tl.types import InputMessagesFilterDocument




LOGS.info("Dil dosyası yükleniyor...")
LANGUAGE_JSON = None



if LANGUAGE_JSON == None:
    if path.isfile(f"./userbot/language/{LANGUAGE}.xjson"):
        try:
            LANGUAGE_JSON = loads(open(f"./userbot/language/{LANGUAGE}.xjson", "r",encoding='utf-8').read())
        except JSONDecodeError:
            raise Exception("Invalid json file")
    else:
        if path.isfile("./userbot/language/DEFAULT.xjson"):
            LOGS.warn("Varsayılan dil dosyası kullanılıyor...")
            LANGUAGE_JSON = loads(open(f"./userbot/language/DEFAULT.xjson", "r").read())
        else:
            raise Exception(f"Didn't find {LANGUAGE} file")

LOGS.info(f"{LANGUAGE_JSON['LANGUAGE']} dili yüklendi.")

def get_value (plugin = None, value = None):
    global LANGUAGE_JSON

    if LANGUAGE_JSON == None:
        raise Exception("Please load language file first")
    else:
        if not plugin == None or value == None:
            Plugin = LANGUAGE_JSON.get("STRINGS").get(plugin)
            if Plugin == None:
                raise Exception("Invalid plugin")
            else:
                String = LANGUAGE_JSON.get("STRINGS").get(plugin).get(value)
                if String == None:
                    return Plugin
                else:
                    return String
        else:
            raise Exception("Invalid plugin or string")
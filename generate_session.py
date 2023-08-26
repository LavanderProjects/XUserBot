from pyrogram import Client

with Client("XUserBot", API_ID, API_HASH, in_memory = True) as cli:
  SESSION = cli.export_session_string()
  print(SESSION)

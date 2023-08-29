from pyrogram import Client

with Client("XUserBot", 26921440,"483adff3ca0cf539332960147b0ef8ff", in_memory = True) as cli:
  SESSION = cli.export_session_string()
  print(SESSION)

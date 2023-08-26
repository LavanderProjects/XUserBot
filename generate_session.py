from pyrogram import Client

with Client("XUserBot", 1038911,"94d21cd31f1d54ff715ead95b1777bc1") as cli:
  SESSION = cli.export_session_string()
  print(SESSION)

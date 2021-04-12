# import logging
from pyrogram import Client, idle

app = Client("tgvc")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED by @mr_srlock')
idle()
app.stop()
print('\n>>> USERBOT STOPPED by @mr_srlock')

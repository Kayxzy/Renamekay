import asyncio
from pyrogram import Client, __version__ 
from pyrogram import compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5979614687:AAHbj6UprKT9hq7jSOSBMS4Ln683EwSEdJg")

API_ID = int(os.environ.get("API_ID", "18971259"))

API_HASH = os.environ.get("API_HASH", "3f1373ede58a6d52d89ec0f8700fd688")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()

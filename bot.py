import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5979614687:AAHbj6UprKT9hq7jSOSBMS4Ln683EwSEdJg")

API_ID = int(os.environ.get("API_ID", "17131033"))

API_HASH = os.environ.get("API_HASH", "7768488c115ac09684bb38e608c47997")

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

from pyrogram import Client, emoji, filters
from pyrogram.errors import FloodWait
from pyrogram import Client
import datetime
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)

from pyrogram.types import ChatPermissions
####Abdusattorov####
import time
from time import sleep
import random
 
api_id =  input('api_id kirit')
api_hash = input('api_hash kirit: ')


app = Client("#SLOPPY", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.command("write", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".write ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be writed
    typing_symbol = "...✍️"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 3):
        try:
            text = "🔥🔥🔥🔥🔥🔥🔥🔥🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥" + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0


@app.on_message(filters.command("help", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 20):
        try:
            text = "WAIT..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🆘HELP FOR SLOPPY🕹\n\nAssalomu Aleykum Foydalanuvchi🖐\n\nSLOPPY Userbotiga xush kelibsiz🤝\n\nUserbot 100% xavfsiz va sodda✌️\n➖➖➖➖➖➖➖➖➖➖➖➖\n              👇Functions👇\n\n.help  UserBot haqida📝\n\n.heart  animatsiya❤‍🔥\n\n.write  dan keyin probel tashab so‘z yozasiz, yozgan so‘zingiz animatsiya bo‘ladi✍\n\n.juma  Juma tabrik 🌙\n\n.police Politsiya avtomobil chirog‘i🚨\n\n.time   Hozirgi Sana📆 va vaqt ⏰\n\n.sloppy  SLOPPY🖼\n\nSLOPPY USERBOT BY @AbdusattorovJ\nSLOPPY Kanali: @SLOPPYUserBot")
    perc = 0

@app.on_message(filters.command("hello", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 20):
        try:
            text = "WAIT..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("╔┓┏╦━╦┓╔┓╔━━╗\n║┗┛║┗╣┃║┃║X X  ║\n║┏┓║┏╣┗╣┗╣╰╯║\n╚┛┗╩━╩━╩━╩━━╝")
    perc = 0

@app.on_message(filters.command("sloppy", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 20):
        try:
            text = "WAIT..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥⬜️⬜️🟥⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
    perc = 0

@app.on_message(filters.command("juma", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 3):
        try:
            text = "▫️▫️▫️▫️▫️" + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("▫️▫️▫️▫️▫️")
    sleep(0.01)
 
    msg.edit("▫️▫️▫️▫️◾️")
    perc = 0

    msg.edit("▫️▫️▫️◾️◾️")
    sleep(0.01)
 
    msg.edit("▫️▫️◾️◾️◾️")
    perc = 0

    msg.edit("▫️◾️◾️◾️◾️")
    sleep(0.01)
 
    msg.edit("◾️◾️◾️◾️◾️")
    perc = 0

    msg.edit("▫️▫️▫️▫️▫️")
    sleep(0.01)
 
    msg.edit("▫️▫️▫️▫️◾️")
    perc = 0

    msg.edit("▫️▫️▫️◾️◾️")
    sleep(0.01)
 
    msg.edit("▫️▫️◾️◾️◾️")
    perc = 0

    msg.edit("▫️◾️◾️◾️◾️")
    sleep(0.01)
 
    msg.edit("◾️◾️◾️◾️◾️")
    perc = 0

    msg.edit("▫️▫️▫️▫️▫️")
    sleep(0.01)
 
    msg.edit("▫️▫️▫️▫️◾️")
    perc = 0

    msg.edit("▫️▫️▫️◾️◾️")
    sleep(0.01)
 
    msg.edit("▫️▫️◾️◾️◾️")
    perc = 0

    msg.edit("▫️◾️◾️◾️◾️")
    sleep(0.01)
 
    msg.edit("◾️◾️◾️◾️◾️")
    perc = 0

    msg.edit("💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    sleep(0.01)
 
    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💣💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💣💣💣💥💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    perc = 0

    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💥💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💣💣💥💣\n💣💣💥💣💣💣💣💣💥💣💣\n💥💥💥💣💣💣💣💣💣💣💥")
    sleep(0.01)
 
    msg.edit("💥💣💥💣💥💣💥💣💣💣💣\n💥💣💥💥💣💣💣💥💣💣💥\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💥💣💥💣\n💣💣💥💣💥💣💥💣💥💣💣\n💥💥💥💣💣💣💥💣💥💣💥")
    perc = 0

    msg.edit("💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥")
    sleep(0.01)

    msg.edit("💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    sleep(0.01)
 
    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💣💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💣💣💣💥💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    perc = 0

    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💥💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💣💣💥💣\n💣💣💥💣💣💣💣💣💥💣💣\n💥💥💥💣💣💣💣💣💣💣💥")
    sleep(0.01)
 
    msg.edit("💥💣💥💣💥💣💥💣💣💣💣\n💥💣💥💥💣💣💣💥💣💣💥\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💥💣💥💣\n💣💣💥💣💥💣💥💣💥💣💣\n💥💥💥💣💣💣💥💣💥💣💥")
    perc = 0

    msg.edit("💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥")
    sleep(0.01)

    msg.edit("💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    sleep(0.01)
 
    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💣💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💣💣💣💥💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    perc = 0

    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💥💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💣💣💥💣\n💣💣💥💣💣💣💣💣💥💣💣\n💥💥💥💣💣💣💣💣💣💣💥")
    sleep(0.01)
 
    msg.edit("💥💣💥💣💥💣💥💣💣💣💣\n💥💣💥💥💣💣💣💥💣💣💥\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💥💣💥💣\n💣💣💥💣💥💣💥💣💥💣💣\n💥💥💥💣💣💣💥💣💥💣💥")
    perc = 0

    msg.edit("💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥")
    sleep(0.01)

    msg.edit("💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    sleep(0.01)
 
    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💣💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💣💣💣💥💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    perc = 0

    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💥💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💣💣💥💣\n💣💣💥💣💣💣💣💣💥💣💣\n💥💥💥💣💣💣💣💣💣💣💥")
    sleep(0.01)
 
    msg.edit("💥💣💥💣💥💣💥💣💣💣💣\n💥💣💥💥💣💣💣💥💣💣💥\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💥💣💥💣\n💣💣💥💣💥💣💥💣💥💣💣\n💥💥💥💣💣💣💥💣💥💣💥")
    perc = 0

    msg.edit("💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)
#police
@app.on_message(filters.command("police", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 3):
        try:
            text = "1..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("1...")
    sleep(0.01)
 
    msg.edit("2...")
    perc = 0

    msg.edit("3...")
    sleep(0.01)
 
    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)
now = datetime.datetime.now()
@app.on_message(filters.command("time", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0

    while(perc < 20):
        try:
            text = "WAIT..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit(now.strftime("Hozir Sana📆: %Y-%m-%d \nSoat⏰: %H:%M:%S"))
    perc = 0

app.run()
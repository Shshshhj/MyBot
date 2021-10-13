import pyrogram
import random

from pyrogram import Client, filters
from pyrogram.types import User, Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

#=======================================================================

START_MSG = '<b>Hai {},\nIam A Simple Bot</b>>'

START_IMG = ["https://telegra.ph/file/00b0aa858250ec4229e54.jpg",
         "https://telegra.ph/file/eb6f76fbd5c3228d7babe.jpg",
         "https://telegra.ph/file/5b7a670096a54e3183b51.jpg",]

#=======================================================================


Sam = Client(api_id=1234567,
            session_name="Samantha",
            api_hash="t5h8a4ndg9ba59mgs58lo2h90ndr72bins",                      
            bot_token="61952638:AbCdEfGhIjKlMnOp")

#=======================================================================

@Sam.on_message(filters.command(['start']))
def start(client, cmd):
         buttons = [
                      [
                         InlineKeyboardButton('Help', callback_data="help"),
                         InlineKeyboardButton('Source Code', url='https://github.com/Arun-TG/SampleBot')
                      ],
                      [
                         InlineKeyboardButton('Channel', url='https://t.me/CC_ChannelNew')
                      ]
                   ]
         cmd.reply_photo(photo=random.choice(START_IMG), caption=START_MSG.format(cmd.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons))
               
         
#=======================================================================

@Sam.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id
        pass
    if (clicked == typed):
                  if query.data == "help":
                           await query.message.edit(text="No Help 😏")

#=======================================================================

Sam.run()

#=======================================================================

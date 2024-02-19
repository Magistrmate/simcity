import json
import os
import threading

import firebase_admin
import telebot
from firebase_admin import credentials, db
from telebot.util import quick_markup

cred = credentials.Certificate(json.loads(os.environ['KEY']))
firebase_admin.initialize_app(
    cred,
    {'databaseURL': 'https://simcity-e2af7-default-rtdb.firebaseio.com/'})

bot = telebot.TeleBot(os.environ['TOKEN'])


def bot_check():
 return bot.get_me()


# def bot_runner():


@bot.message_handler(func=lambda _message: True)
def echo_message(message):
    markup = quick_markup(
     {
         'Металл': {
             'callback_data': 'https://twitter.com'
         },
         'Древесина': {
             'callback_data': 'https://facebook.com'
         },
         'Пластмасса': {
             'callback_data': 'whatever'
         },
         'Пластмасса': {
              'callback_data': 'whatever'
          },
         'рке': {
              'callback_data': 'whatever'
          },
         'рерно': {
              'callback_data': 'whatever'
          }
         
     })
    bot.reply_to(message, message.text, reply_markup=markup)
    db.reference('/user/1').set(message.text)

bot.infinity_polling(none_stop=True)

t = threading.Thread(target=bot_runner)
t.start()

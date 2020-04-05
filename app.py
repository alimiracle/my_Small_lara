from telegram.ext import MessageHandler, Filters

from telegram.ext import CommandHandler
from telegram.ext import Updater
import logging
import requests
from bot_config import *
def send_post(text):

    url="http://localhost:5000/get"

    myobj = {'text': text}

    x = requests.post(url, data = myobj)

    return x.text
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
def echo(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text=send_post(update.message.text))

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()


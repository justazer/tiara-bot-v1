from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from config import TOKEN
from config import PORT
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update:Update, context:CallbackContext):

    update.message.reply_text("Hi ayang {}, hari ini kamu sehat kannn? 😊".format(update.message.from_user.first_name))


if __name__ == '__main__':
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://tiarabot.herokuapp.com/'+ TOKEN)
    updater.idle()



def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

def send_findig(update:Update, message):
    update.message.reply_text(message, '(placeholder text)')

def send_help(update:Update, message):
    update.message.reply_text(message, 'ALPHA = FEATURES MAY NOT WORK')

dp.add_handler(CommandHandler("findig", send_findig))
dp.add_handler(CommandHandler("help", send_help))


# @bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# # lambda function finds messages with the '@' sign in them
# # in case msg.text doesn't exist, the handler doesn't process it
# def at_converter(message):
#     texts = message.text.split()
#     at_text = findat(texts)
#     if at_text == '@': # in case it's just the '@', skip
#         pass
#     else:
#         insta_link = "https://instagram.com/{}".format(at_text[1:])
#         bot.reply_to(message, insta_link)

# while True:
#     try:
#         bot.polling(none_stop=True)
#         # ConnectionError and ReadTimeout because of possible timout of the requests library
#         # maybe there are others, therefore Exception
#     except Exception:
#         time.sleep(15)
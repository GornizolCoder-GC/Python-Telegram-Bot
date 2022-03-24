import logging
from settings.settings import BOT_TOKEN
from telegram.ext import Filters, Updater, CallbackContext, CommandHandler, MessageHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
updater = Updater(token=BOT_TOKEN, use_context=True)

logging.info("botni holati")
print(updater.bot.get_me())


def start(update: Updater, context: CallbackContext):
    logging.info("/start komandasi bosildi!")
    updater.bot.sendMessage(chat_id=update.effective_chat.id, text="Salom")
def get_info(update: Updater, context: CallbackContext):
    logging.info("/help komandasi bosildi!")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/start - botni ishga tushiruvchi komanda"
                                                                    "\n/help - komanda va buyruqlar haqida ma`lumot olish")
def echo_bot(update: Updater, context: CallbackContext):
    logging.info("echobot ishga tushirildi!")
    caps = update.message.text.upper()
    context.bot.send_message(chat_id = update.effective_chat.id, text=caps)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', get_info))
updater.dispatcher.add_handler(MessageHandler(Filters.text &(~Filters.command), echo_bot))

updater.start_polling()
updater.idle()

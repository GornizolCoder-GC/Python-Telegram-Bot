from settings.settings import BOT_TOKEN
from telegram.ext import CommandHandler, Updater, CallbackContext


updater = Updater(BOT_TOKEN, use_context=True)

def to_upp(update: Updater, context: CallbackContext):
    caps = ' '.join(context.args).upper()
    updater.bot.send_message(chat_id = update.effective_chat.id, text=caps)

def to_low(update: Updater, context: CallbackContext):
    low = ' '.join(context.args).lower()
    updater.bot.send_message(chat_id=update.effective_chat.id, text=low)

def get_info(update:Updater, context: CallbackContext):
    updater.bot.send_message(chat_id=update.effective_chat.id, text="/start - botni ishga tushirish."
                            "\n/caps - komanda berilgan matndagi barcha harflarni katta harflarga o'zgartiradi."
                            "\n/low - komanda berigan matndagi barcha harflarni kichik harflarga o'zgartiradi."
                            "\n/help - komanda buyruqlar haqida ma'lumot beradi.")

updater.dispatcher.add_handler(CommandHandler('caps', to_upp))
updater.dispatcher.add_handler(CommandHandler('low', to_low))
updater.dispatcher.add_handler(CommandHandler('help', get_info))

updater.start_polling()
updater.idle()


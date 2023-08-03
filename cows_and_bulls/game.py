# блок импортов
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from telegram import Update
from config import TOKEN
import random

def gateway(update: Update, context: CallbackContext):
    user_name = update.effective_user.first_name
    message = update.message.text  # берет текст сообщения
    with open("cows_and_bulls/words.txt", encoding="utf-8") as file:
        words = file.read().split('\n') # получаем список слов 
    secret_word = random.choice(words) # выбираем случайное слово
    context.user_data["секрет"] = secret_word
    update.message.reply_text(secret_word)

# блок обработчиков
message_handler = MessageHandler(Filters.text, gateway)

# сам бот и его зам
updater = Updater(TOKEN)  # ядро нашего бота
dispatcher = updater.dispatcher  # распределяет сообщения по хэндлерам

# добавление хэндлеров диспетчеру
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()

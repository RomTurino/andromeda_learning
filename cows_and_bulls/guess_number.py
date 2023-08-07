# блок импортов
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from telegram import Update
from config import TOKEN
import random

def game(update: Update, context: CallbackContext):
    user_name = update.effective_user.first_name
    my_number = update.message.text
    if "секрет" not in context.user_data:
        secret_number = random.randint(1,100) # выбираем случайное число
        context.user_data["секрет"] = secret_number # записываем
        update.message.reply_text("("Я загадал число от 1 до 100. Попробуй угадай")
    else:
        secret_number = context.user_data["секрет"] #достаем
    if my_number == '/start':
        return None
    elif not my_number.isdigit():
        update.message.reply_text("Вводить можно только числа")
        return None
    my_number = int(my_number)
    if my_number > secret_number:
        update.message.reply_text(f"Мое число меньше")
    elif my_number < secret_number:
        update.message.reply_text(f"Мое число больше")
    else:
        update.message.reply_photo("http://risovach.ru/upload/2014/01/mem/villi-vonka_39555586_orig_.jpeg")
        del context.user_data["секрет"]# убираем секрет из рюкзака
    
# блок обработчиков
message_handler = MessageHandler(Filters.text, game)

# сам бот и его зам
updater = Updater(TOKEN)  # ядро нашего бота
dispatcher = updater.dispatcher  # распределяет сообщения по хэндлерам

# добавление хэндлеров диспетчеру
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()

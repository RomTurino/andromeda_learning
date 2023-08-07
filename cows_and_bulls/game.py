# -*- coding: utf-8 -*- 
# блок импортов
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from telegram import Update
from config import TOKEN
import random

def gateway(update: Update, context: CallbackContext):
    user_name = update.effective_user.first_name
    my_word = update.message.text  # берет текст сообщения
    if "секрет" not in context.user_data:
        with open("cows_and_bulls/words.txt", encoding="utf-8") as file:
            words = file.read().split('\n') # получаем список слов 
        secret_word = random.choice(words) # выбираем случайное слово
        context.user_data["секрет"] = secret_word # записываем
        update.message.reply_text(f"Это - словесная игра 'Быки и коровы'. Я загадал слово из {len(secret_word)} букв. Ваша задача - называть слова из такого же количества букв. Если буква из вашего слова будет в моем - она будет называться коровой. Если же ее место в слове совпадает с моим, то она становится быком. Ваша цель - угадать всё слово. Удачи!")
    else:
        secret_word = context.user_data["секрет"] #достаем
    if my_word != '/start':
        return None
    elif len(secret_word) != len(my_word):
        update.message.reply_text(f"Количество букв должно быть {len(secret_word)}")
        return None
    bulls = 0 # быки, совпадает позиция
    cows = 0 # коровы, буквы просто есть
    for index, letter in enumerate(my_word):
        if letter in secret_word:
            if secret_word[index] == my_word[index]: 
                bulls+=1
            else:
                cows+=1
    update.message.reply_text(f"В вашем слове {bulls} быков и {cows} коров")
    if bulls == len(secret_word):
        update.message.reply_photo("http://risovach.ru/upload/2014/01/mem/villi-vonka_39555586_orig_.jpeg")
        del context.user_data["секрет"] # убираем секрет из рюкзака
# блок обработчиков
message_handler = MessageHandler(Filters.text, gateway)

# сам бот и его зам
updater = Updater(TOKEN)  # ядро нашего бота
dispatcher = updater.dispatcher  # распределяет сообщения по хэндлерам

# добавление хэндлеров диспетчеру
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()

# блок импортов
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    ConversationHandler
)
from telegram.ext.filters import Filters
from telegram import Update
from config import TOKEN

NAME, SURNAME, NUMBER = range(3)

# блок функций
def start(update: Update, context: CallbackContext):
    # update - входящее сообщение, context - это чат в целом
    bot_name = context.bot.name
    update.message.reply_text(f"Я бот, меня зовут {bot_name}")
    update.message.reply_text("Начинаю сбор информации. Назови своё имя")
    return NAME # переход к следующему шагу
    
def end(update: Update, context: CallbackContext):
    update.message.reply_text(f"Значит, ты выбрал конец")

def get_name(update: Update, context: CallbackContext):
    name = update.message.text
    context.user_data["name"] = name # записываем
    update.message.reply_text(f"Вы ввели имя {name}")
    update.message.reply_text(f"Теперь введите фамилию")
    return SURNAME

def get_surname(update: Update, context: CallbackContext):
    name = context.user_data["name"] # достаем
    surname = update.message.text
    context.user_data["surname"] = surname
    update.message.reply_text(f"Вас зовут {name} {surname}")
    return NUMBER

def get_number(update: Update, context: CallbackContext):
    number = update.message.text
    if not number.isdigit():
        update.message.reply_text("Введите номер в формате 8xxxxxxxxxx")
        return None
    context.user_data["number"] = number
    name = context.user_data["name"]
    surname = context.user_data["surname"]
    update.message.reply_text(f"Сбор информации завершен. Вот ваш контакт. Запишите его")
    update.message.reply_contact(number, name, surname)
    return ConversationHandler.END # завершить разговор

#сам бот и его зам
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# хэндлеры
contact_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)], # точка входа
    states={
            NAME:[MessageHandler(Filters.text, get_name)],
            SURNAME:[MessageHandler(Filters.text, get_surname)]
        }, # шаги разговора
    fallbacks=[CommandHandler("no", end)] # точка выхода
)
#добавляем хэндлеры диспетчеру
dispatcher.add_handler(contact_handler)

print("Server started")
updater.start_polling()
updater.idle()
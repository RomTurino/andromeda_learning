# блок импортов
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    ConversationHandler
)
from telegram.ext.filters import Filters
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import TOKEN

GENDER, NAME, SURNAME, NUMBER = range(4)
MALE, FEMALE, OTHER = "мужской", "женский", "другой"

# блок функций
def start(update: Update, context: CallbackContext):
    # update - входящее сообщение, context - это чат в целом
    keyboard = [[MALE, FEMALE, OTHER]] # разметка
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите ваш пол")
    bot_name = context.bot.name
    update.message.reply_text(f"Я бот, меня зовут {bot_name}", reply_markup=markup)
    update.message.reply_text("Начинаю сбор информации. Выбери свой пол или нажми /end, чтобы прекратить разговор")
    return GENDER # переход к следующему шагу
    
def end(update: Update, context: CallbackContext):
    update.message.reply_text(f"Значит, ты выбрал конец")
    return ConversationHandler.END

def get_gender(update: Update, context: CallbackContext):
    gender = update.message.text 
    context.user_data["gender"] = gender
    update.message.reply_text("Попрошу Вас ввести имя", reply_markup=ReplyKeyboardRemove())
    return NAME

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
            GENDER:[MessageHandler(Filters.regex(f"^({MALE}|{FEMALE}|{OTHER})$"), get_gender)],
            NAME:[MessageHandler(Filters.text & ~Filters.command, get_name)],
            SURNAME:[MessageHandler(Filters.text & ~Filters.command, get_surname)],
            NUMBER:[MessageHandler(Filters.text & ~Filters.command, get_number)]
        }, # шаги разговора
    fallbacks=[CommandHandler("end", end)] # точка выхода
)
#добавляем хэндлеры диспетчеру
dispatcher.add_handler(contact_handler)

print("Server started")
updater.start_polling()
updater.idle()
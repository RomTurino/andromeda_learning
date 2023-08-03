# блок импортов
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from telegram import Update
from config import TOKEN
import random


def make_eval(update: Update, context: CallbackContext, message: list):
    if not message or len(message) != 2:
        update.message.reply_text(
            "Введите два числа через пробел после команды")
        return None
    num1, num2 = message
    if not num1.isdigit() or not num2.isdigit():
        update.message.reply_text("Вводить можно только числа")
        return None
    num1, num2 = int(num1), int(num2)
    return num1, num2


def plus(update: Update, context: CallbackContext):
    message = context.args  # ["слова", "после", "команды"]
    num1, num2 = make_eval(update, context, message)
    result = num1 + num2
    update.message.reply_text(f"Это будет {result}")


def minus(update: Update, context: CallbackContext):
    message = context.args  # ["слова", "после", "команды"]
    num1, num2 = make_eval(update, context, message)
    result = num1 - num2
    update.message.reply_text(f"Это будет {result}")


def multiply(update: Update, context: CallbackContext):
    message = context.args  # ["слова", "после", "команды"]
    num1, num2 = make_eval(update, context, message)
    result = num1 * num2
    update.message.reply_text(f"Это будет {result}")


def divide(update: Update, context: CallbackContext):
    message = context.args  # ["слова", "после", "команды"]
    num1, num2 = make_eval(update, context, message)
    if num2 == 0:
        update.message.reply_text("На ноль делить нельзя")
        return None
    result = num1 / num2
    update.message.reply_text(f"Это будет {result}")


def gateway(update: Update, context: CallbackContext):
    user_name = update.effective_user.first_name
    message = update.message.text  # берет текст сообщения
    if message == "привет":
        update.message.reply_text(f"Привет, {user_name}")
    elif message == "пока":
        update.message.reply_text(f"Пока, {user_name}")
    elif "красн" in message:
        update.message.reply_text("Красный - это мой любмый цвет")
    elif message == "как дела":
        answers = ["нормально", "плохо", "пучком", "ничего"]
        update.message.reply_text(f"У меня {random.choice(answers)}, а у тебя?")
    elif "❤️" in message:
        update.message.reply_text("Я вижу у тебя сердечко в сообщении, это так мило")
    elif "политик" in message:
        answers = ["не хочу говорить о политике", "Я за коммунизм", "Ой, давай сменим тему"]
        update.message.reply_text(f"А{random.choice(answers)}")


# блок обработчиков
minus_handler = CommandHandler("minus", minus)
plus_handler = CommandHandler("plus", plus)
multiply_handler = CommandHandler("multiply", multiply)
divide_handler = CommandHandler("divide", divide)
message_handler = MessageHandler(Filters.text, gateway)

# сам бот и его зам
updater = Updater(TOKEN)  # ядро нашего бота
dispatcher = updater.dispatcher  # распределяет сообщения по хэндлерам

# добавление хэндлеров диспетчеру
dispatcher.add_handler(plus_handler)
dispatcher.add_handler(minus_handler)
dispatcher.add_handler(multiply_handler)
dispatcher.add_handler(divide_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()

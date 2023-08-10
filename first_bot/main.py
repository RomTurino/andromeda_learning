# блок импортов
from pathlib import Path
from config import TOKEN
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update


# блок функций


def start(update: Update, context: CallbackContext):
    # update - входящее сообщение, context - это чат в целом
    bot_name = context.bot.name
    update.message.reply_text(f"Я бот, меня зовут {bot_name}")
    update.message.reply_text(f"""
                              Вот что я умею:
                              /hello - я поздороваюсь с тобой
                              /bye - я попрощаюсь с тобой
                              /contact - даст номер Илона Маска
                              /help - покажу еще раз эту справку
                              """)


def send_contact(update: Update, context: CallbackContext):
    update.message.reply_contact("8(937)-582-84-45", "Илон", "Маск")


def hello(update: Update, context: CallbackContext):
    user_name = update.effective_user.last_name
    update.message.reply_photo(
        "https://mega-u.ru/wp-content/uploads/2023/03/113-5.jpg")
    update.message.reply_text(f"Ну привет, {user_name}")


def bye(update: Update, context: CallbackContext):
    user_name = update.effective_user.first_name
    context.bot.send_message(update.effective_chat.id, f"Пока, {user_name}")


def echo(update: Update, context: CallbackContext):
    message = context.args # то, что написано после команды
    if not message:  # если сообщение пустое
        update.message.reply_text(
            "После команды /echo нужно набрать сообщение через пробел")
        return None
    message = " ".join(message) # объединяем список в строку
    update.message.reply_text(message)
    print(message)


def animation(update: Update, context: CallbackContext):  # callback-функция
    update.message.reply_animation(
        "https://cdn.trinixy.ru/uploads/posts/2021-01/1610009179_gifs_11.gif")




def send_music(update: Update, context: CallbackContext):
    update.message.reply_audio(Path("first_bot/audio/amazing.mp3").read_bytes())



# блок обработчиков (хэндлеров)
start_handler = CommandHandler("start", start)
hello_handler = CommandHandler("hello", hello)
bye_handler = CommandHandler("bye", bye)
help_handler = CommandHandler("help", start)
contact_handler = CommandHandler("contact", send_contact)
echo_handler = CommandHandler("echo", echo)
animation_handler = CommandHandler("animation", animation)
music_handler = CommandHandler("music", send_music)


# сам бот и его зам
updater = Updater(TOKEN)  # ядро нашего бота
dispatcher = updater.dispatcher  # распределяет сообщения по хэндлерам

# работники диспетчера
dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(bye_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(contact_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(animation_handler)
dispatcher.add_handler(music_handler)


print("Бот запущен")
updater.start_polling()  # запускает обновления
updater.idle()

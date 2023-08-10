# -*- coding: utf-8 -*-
# блок импортов
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler
from telegram.ext.filters import Filters
from config import TOKEN
from functions import *


 

# блок обработчиков
game_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        LEVEL:[MessageHandler(Filters.regex(f"^({GO})$"), choose_level)],
        BEGIN:[MessageHandler(Filters.regex(f"^({EASY}|{MEDIUM}|{HARD})$"), begin)],
        GAME: [MessageHandler(Filters.text & ~Filters.command, game)]
    },
    fallbacks=[CommandHandler("cancel", cancel),
               CommandHandler("stop", cancel)]
)

# сам бот и его зам
updater = Updater(TOKEN)  # ядро нашего бота
dispatcher = updater.dispatcher  # распределяет сообщения по хэндлерам

# добавление хэндлеров диспетчеру
dispatcher.add_handler(game_handler)


updater.start_polling()
updater.idle()

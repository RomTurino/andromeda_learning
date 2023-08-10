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


#сам бот и его зам
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# хэндлеры
game_handler = ConversationHandler(
    entry_points=[], # точка входа
    states={
            
            }, # шаги разговора
    fallbacks=[] # точка выхода
)
#добавляем хэндлеры диспетчеру
dispatcher.add_handler(game_handler)

print("Server started")
updater.start_polling()
updater.idle()
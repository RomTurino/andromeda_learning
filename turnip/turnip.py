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
import pymorphy2
import time

BEGIN, GAME, VICTORY = range(3)
GO = 'Вперед'
morph = pymorphy2.MorphAnalyzer()
CHARACTERS = {
    "кот":"https://starwars-galaxy.ru/800/600/https/linedot.ru/wp-content/uploads/2019/04/kartinki-koshek_32.jpg",
    "кошка": "https://starwars-galaxy.ru/800/600/https/linedot.ru/wp-content/uploads/2019/04/kartinki-koshek_32.jpg"
}

#блок функций
def start(update: Update, context: CallbackContext):
    keyboard = [[GO]]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("Давай поиграем. Ты любишь придумывать сказки? Я - очень люблю. Ты знаешь сказку, как посадил дед репку? А кто помогал её тянуть?",
                              reply_markup=markup)
    heroes = [["дедку"], ["дедка", "репку"]] # стэк персонажей
    context.user_data["heroes"] = heroes
    return BEGIN

def begin(update: Update, context: CallbackContext):
    update.message.reply_text("Посадил дед репку. Выросла репка большая-пребольшая. Тянет-потянет - вытянуть не может. Кого позвал дед?",
                              reply_markup=ReplyKeyboardRemove())
    return GAME

def game(update: Update, context: CallbackContext):
    word = update.message.text
    tag = morph.parse(word)[0] # тег, состоящий из граммем (число, падеж, род и т.д.)
    if tag.tag.animacy != "anim":# == "inan"
        update.message.reply_text(f"Долго звали мы {tag.normal_form}: никого не дозвались")
        return None
    nomn = tag.inflect({'nomn'}).word # слово в именительном падеже
    accs = tag.inflect({'accs'}).word # слово в винительном падеже
    if nomn in CHARACTERS:
        update.message.reply_photo(CHARACTERS[nomn])
        update.message.reply_text(f"Привет! Я - {nomn}. Буду помогать")
        time.sleep(2)
    heroes = context.user_data["heroes"]
    heroes[0].insert(0, nomn)
    heroes.insert(0, [accs])
    # собираем в одну строку
    result = ""
    for nom, ac in heroes[1:]: #не берем [бабку]
        result += f'{nom} - за {ac}.'.title() # title - первая буква заглавная
    update.message.reply_text(result)
    if "мыш" in nomn:
        return victory(update, context)
    update.message.reply_text("Тянут-потянут - вытянуть не могут!")
    update.message.reply_text(f"Кого позвал {nomn}?")
    
    

def victory(update: Update, context: CallbackContext):
    update.message.reply_text("Тянут-потянут... И вытянули репку! А хотите сыграть еще? Нажмите для этого на /start")
    return ConversationHandler.END

def end(update: Update, context: CallbackContext):
    update.message.reply_text(f"Значит, ты выбрал конец")
    return ConversationHandler.END

#сам бот и его зам
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# хэндлеры
game_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)], # точка входа
    states={
                BEGIN:[MessageHandler(Filters.regex(f"^({GO})$"), begin)],
                GAME:[MessageHandler(Filters.text & ~Filters.command, game)]
            }, # шаги разговора
    fallbacks=[CommandHandler('end', end)] # точка выхода
)
#добавляем хэндлеры диспетчеру
dispatcher.add_handler(game_handler)

print("Server started")
updater.start_polling()
updater.idle()
from telegram import ReplyKeyboardMarkup
import pymorphy2

GO = "Вперед"
LEVEL, BEGIN, GAME = range(3)
morph = pymorphy2.MorphAnalyzer()
COW = morph.parse("корова")[0]
BULL = morph.parse("бык")[0]


# надписи на кнопках уровнях сложности
EASY = "easy"
MEDIUM = "medium"
HARD = "hard"
CANCEL = "/cancel"

# количество букв по уровням
LEVELS = {
    EASY: 4,
    MEDIUM: 5,
    HARD: 6
}

KEYPAD = ReplyKeyboardMarkup([[CANCEL]],
                             resize_keyboard=True,
                             input_field_placeholder="Чтобы сдаться, нажми на /cancel")

# стоимость слов на уровнях
MEDIUM_PRICE = 5
HARD_PRICE = 6

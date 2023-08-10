# блок импортов
from telegram.ext import  CallbackContext, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
import random
from constants import *
import rsa
from stickers import *

def start(update: Update, context: CallbackContext):
    keyboard = [[GO]]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_sticker(random.choice(HELLO_STIC))
    update.message.reply_text(
        'В этой игре компьютер загадывает слово, и говорит тебе, сколько в нем букв')
    update.message.reply_text('Ты говоришь слово из такого же количества букв')
    update.message.reply_text(
        'Если у какой-то из букв твоего совпадает позиция с буквой из загаданного слова - это бык')
    update.message.reply_text(
        'Если просто такая буква есть в слове - это корова')
    update.message.reply_text("Твоя цель - отгадать загаданное слово")
    update.message.reply_text(
        f'Чтобы начать, нажми на "{GO}", чтобы выйти - нажмите на /cancel', reply_markup=markup)
    return LEVEL

def choose_level(update: Update, context: CallbackContext):
    with open("cows_and_bulls_update/ssh/key", encoding="utf-8") as file:
        private_key = file.read().split(', ')
        private_key = [int(number) for number in private_key]
        private_key = rsa.PrivateKey(*private_key)
    with open(f"cows_and_bulls_update/coins.txt", encoding="utf-8") as file:
        money = file.read()
        message = rsa.decrypt(money, private_key)
        money = message.decode('utf8')
    context.user_data["money"] = int(money) # монеты в рюкзаке
    context.user_data["attempts"] = 0 # попытки в рюкзаке
    update.message.reply_text(f"У вас {money} монет. Слово уровня easy: бесплатно, medium: {MEDIUM_PRICE} монет, hard: {HARD_PRICE}. Награда за отгаданное слово = количеству букв в слове.")
    keyboard = [[EASY, MEDIUM, HARD]]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, input_field_placeholder="Выбирай, что тебе по силам")
    update.message.reply_text("Выбери уровень сложности", reply_markup=markup)
    return BEGIN
    
    

def begin(update: Update, context: CallbackContext):
    money = context.user_data["money"]
    difficulty = update.message.text # считываем текст кнопки (easy)
    if (money < MEDIUM_PRICE and difficulty == MEDIUM) or (money < HARD_PRICE and difficulty == HARD):
        difficulty = EASY
        update.message.reply_text("У вас недостаточно средств. Включен уровень простой")
    elif difficulty == MEDIUM:
        money -= MEDIUM_PRICE
        update.message.reply_text(f"Взяли оплату {MEDIUM_PRICE}. Теперь у вас {money} монет")   
    elif difficulty == HARD:
        money -= HARD_PRICE
        update.message.reply_text(f"Взяли оплату {HARD_PRICE}. Теперь у вас {money} монет")   
        
    context.user_data["difficulty"] = difficulty  # сохранили в рюкзак выбранный уровень сложности 
        
    
    count = LEVELS[difficulty] # в словаре находим, что на easy стоит число 3.
    with open(f"cows_and_bulls_update/{difficulty}_{count}_letters.txt", encoding="utf-8") as file:
        words = file.read().split('\n')  # получаем список слов
    secret_word = random.choice(words)  # выбираем случайное слово
    context.user_data["секрет"] = secret_word  # записываем
    update.message.reply_text(f"Введите слово из {count} букв или сдайтесь, нажав на /cancel", reply_markup=KEYPAD)
    return GAME

def cancel(update: Update, context: CallbackContext):
    if "секрет" in context.user_data:
        secret_word = context.user_data["секрет"]
        update.message.reply_text(f'Загаданное слово было {secret_word}')
        change_money(context,plus=False)
    else:        
        update.message.reply_sticker(random.choice(END_STIC))
        update.message.reply_text(
            "Уже уходите? Буду рад, если вы вернетесь. Чтобы еще поиграть, нажми на /start", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def game(update: Update, context: CallbackContext):
    user_name = update.effective_user.first_name
    my_word = update.message.text  # берет текст сообщения
    secret_word = context.user_data["секрет"]  # достаем
    # update.message.reply_text(f"Секретное слово - {secret_word}, количество букв в нем - {len(secret_word)}")
    if len(secret_word) != len(my_word):
        update.message.reply_text(
            f"Количество букв должно быть {len(secret_word)}", reply_markup=KEYPAD)
        return None
    bulls = 0  # быки, совпадает позиция
    cows = 0  # коровы, буквы просто есть
    for index, letter in enumerate(my_word):
        if letter in secret_word:
            if secret_word[index] == my_word[index]:
                bulls += 1
            else:
                cows += 1
    word_cow = incline_words(COW, cows)
    word_bull = incline_words(BULL, bulls)
    update.message.reply_text(f"В вашем слове {bulls} {word_bull} и {cows} {word_cow}. Если сдаетесь - /cancel", reply_markup=KEYPAD)
    if bulls == len(secret_word):
        update.message.reply_photo(
            "http://risovach.ru/upload/2014/01/mem/villi-vonka_39555586_orig_.jpeg", reply_markup=ReplyKeyboardRemove())
        del context.user_data["секрет"]  # убираем секрет из рюкзака
        change_money(context, plus=True)
        
def change_money(context, plus=False): # если выключатель включен, то прибавляет, выключен - отнимаем
    difficulty = context.user_data["difficulty"]
    money = context.user_data["money"]
    if plus == False: #если мы вычитаем
        money *= -1 # делаем число отрицательным
    money += difficulty # прибавляем или отнимаем монеты
    with open("cows_and_bulls_update/ssh/key.pub", encoding="utf-8") as file:
        public_key = file.read().split(', ')
        public_key = [int(number) for number in public_key]
        public_key = rsa.PublicKey(*public_key)
    with open(f"cows_and_bulls_update/coins.txt", mode="w", encoding="utf-8") as file:
        message = f"{money}".encode('utf8')
        crypto = rsa.encrypt(message, public_key)
        file.write(f"{crypto}")
    
def incline_words(animal:pymorphy2.analyzer.Parse, count:int):
    
    if count == 1:
        animal = animal.inflect({"nomn"}).word #бык, корова
    elif count in [2,3,4]:
        animal = animal.inflect({"gent"}).word   #быка, коровы
    else:
        animal = animal.inflect({"gent", "plur"}).word #быков, коров
    return animal # возвращаем один из вариантов (можно записать в переменную)
    
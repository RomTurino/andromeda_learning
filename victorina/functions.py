# блок импортов
from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from constants import *
import csv
import random



def read_csv():
    with open("victorina/database.csv", encoding="utf-8") as file:
        read_data = list(csv.reader(file, delimiter="|"))
        return read_data

def write_to_csv(row):
    with open("victorina/database.csv", mode="a", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="|", lineterminator="\n")
        writer.writerow(row)
        
def start(update:Update, context:CallbackContext):
    keyboard = [[GO]]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_message(update.effective_chat.id,
                             'Добро пожаловать в викторину. Отвечай на вопросы, выбирая одну из четырех кнопок')
    update.message.reply_text(f"Для продолжения нажми на '{GO}'", reply_markup=markup)
    questions_list = read_csv() # список, внутри которого [вопрос, ответ1, ответ2, ответ3, ответ4]
    random.shuffle(questions_list) # перемешиваем вопросы
    #длина = 5 вопросов, если такое количество есть, либо сколько вопросов есть в файле
    length = QUESTIONS_ON_ROUND if len(questions_list) > QUESTIONS_ON_ROUND else len(questions_list)
    
    questions_list = questions_list[:length] # делаем срез
    context.user_data["questions"] = questions_list
    context.user_data["index"] = 0 # номер первого вопроса
    return GAME

def cancel(update:Update, context:CallbackContext):
    update.message.reply_text("Спасибо за участие в викторине!")
    update.message.reply_text("Нажми на /start, чтобы начать заново")
    return ConversationHandler.END

def game(update:Update, context:CallbackContext):
    questions_list = context.user_data["questions"] 
    index = context.user_data["index"]
    answers = questions_list[index] # это ответы
    question = answers.pop(0) # это вопрос
    update.message.reply_text(question)
    
    

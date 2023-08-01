import functions
# name = input("Who are you? ")
# functions.say_hello(name)
# food = functions.fish_or_chicken()
# print(f"{name} сейчас будет кушать {food}")
questions = functions.read_file("вопросы.txt")
answers = functions.read_file("ответы.txt")
functions.quiz(questions, answers)

def say_hello(name: str):
    """
    Говорит Hello, обращаясь по имени name
    """
    print(f"Hello, {name}")


def fish_or_chicken():
    '''
    Функция даст выбрать курицу или рыбу
    '''
    answer = input("Хочешь курицу или рыбу?")
    need_answers = ["курицу", "рыбу"]
    if answer not in need_answers:
        print("Такого нет в меню")
        return fish_or_chicken()  # запускаем функцию снова
    print(f"Вы выбрали {answer}")
    return answer  # отдаем ответ


def read_file(filename: str):
    with open(filename, encoding="utf-8") as file:  # файл записывается в переменную file
        data_list = file.read().split("\n")  # у file вызывается метод чтения read()
    return data_list  # отдай список
def quiz(questions, answers):
    pass

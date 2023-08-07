import re
text = "мужской"
while True:
    text = input(">>>")
    start = re.findall(r"^муж",text)
    end = re.findall(r"ой$",text)
    if start:
        print("Слово начинается на 'муж'")
    if end:
        print("Слово заканчивается на 'ой'")

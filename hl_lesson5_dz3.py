# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag. Декілька правил: ніяких символів
# з набору string.punctuation не повинно бути, у тому числі й пробілів; підсумкова довжина hashtag має бути
# не більше 140 символів. Кожне слово починається з великої літери. Якщо довжина фінішного хештегу більше
# 140 символів - обрізати підсумковий рядок до 140 символів.

import string

name_str = input("Please enter a string for hashtag: ")
if any(char in string.punctuation for char in name_str):
    for symbol_str in string.punctuation:
        name_str = name_str.replace(symbol_str, " ")
name_str = "#"+name_str.title().replace(" ", "")
if len(name_str) > 140:
    name_str = name_str[:140]
print(f"result hashtag: {name_str}")

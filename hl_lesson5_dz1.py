# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може: починатися з цифри; містити великі літери, пробіл і знаки пунктуації (взяти можна тут string.punctuation),
# окрім нижнього підкреслення "_"; бути жодним із зареєстрованих слів. При цьому повне ім'я змінної повино складатись
# не більш чим з одного нижнього підкреслення "_". Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

import keyword
import string

name_var = input("Please enter a name of variable: ")
result = ""
if name_var:
    result = "True"
    if name_var[0].isdigit():
        result = "False"
    elif keyword.iskeyword(name_var):
        result = "False"
    else:
        for symbol_str in range(len(name_var)):
            if name_var[symbol_str].isupper():
                result = "False"
            elif name_var[symbol_str].isspace():
                result = "False"
            elif name_var[symbol_str] in string.punctuation and name_var[symbol_str] != "_":
                result = "False"
            elif name_var[symbol_str] == "_":
                if symbol_str > 0 and name_var[symbol_str] == name_var[symbol_str-1]:
                    result = "False"
else:
    result = "empty string"
print(f'Name of variable "{name_var}" is {result}')

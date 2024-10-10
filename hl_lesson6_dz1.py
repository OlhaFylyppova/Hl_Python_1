# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string, у якому є string.ascii_letters, з усім набором потрібних букв.

import string

start_string = input("Please enter a range of letters: ")
start_letter = string.ascii_letters.find(start_string[0])
end_letter = string.ascii_letters.find(start_string[2])
result_string = string.ascii_letters[start_letter:end_letter+1]
print(f"result range of letters: {result_string}")

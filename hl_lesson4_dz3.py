# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10. Ваше завдання -
# створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.

import random
rand_list = []
for i in range(random.randint(3, 10)):
    rand_list.append(random.randint(1, 50))
print(f"random list: {rand_list}")
my_list = [rand_list[0], rand_list[2], rand_list[-2]]
print(f"result list: {my_list}")

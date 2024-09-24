# Написати програму, яка просить користувача ввести 4-х значне число з клавіатури,
# після чого друкує на екрані стовпчик цифр, з якого це число складається.

user_number = int(input("Please enter a 4-digit number "))
number_1, number_new = divmod(user_number, 1000)
print(number_1)
number_2, number_new = divmod(number_new, 100)
print(number_2)
number_3, number_4 = divmod(number_new, 10)
print(number_3)
print(number_4)

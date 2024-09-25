# На запит від програми, користувач вводить 5-ти значне ціле, позитивне число.
# Вам необхідно "перевернути" цє число задом наперед, тобто щоб у результаті
# вийшло теж 5-ти значне число, але із зворотною послідовністю цифр.

user_number = int(input("Please enter a 5-digit number "))
number_1, number_new = divmod(user_number, 10000)
number_2, number_new = divmod(number_new, 1000)
number_3, number_new = divmod(number_new, 100)
number_4, number_5 = divmod(number_new, 10)
number_result = number_5*10000+number_4*1000+number_3*100+number_2*10+number_1
print(number_result)

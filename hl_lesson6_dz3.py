# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа,
# поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.

start_number = input("Please enter a number: ")
if start_number.isdigit():
    new_number = start_number
    all_numbers = int(new_number)
    while all_numbers > 9:
        all_numbers = 1
        for number_var in new_number:
            all_numbers *= int(number_var)
        new_number = str(all_numbers)
else:
    all_numbers = "the entered value is not a numeric"
print(f'result: "{start_number}" => {all_numbers}')

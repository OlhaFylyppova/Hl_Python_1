# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче. Тобто,
# потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

continue_run = "y"
while continue_run == "y" or continue_run == "yes":
    user_number_1 = input("Please enter a first number ")
    user_number_2 = input("Please enter a second number ")
    user_operator = input("Please enter a operator (+ or - or * or /) ")
    result_calculation = 0
    flag_point = 0
    result_number_1 = ""
    result_number_2 = ""
    for symbol_number_1 in user_number_1:
        if symbol_number_1.isdigit():
            result_number_1 += symbol_number_1
        elif symbol_number_1 == "." and flag_point == 0:
            result_number_1 += symbol_number_1
            flag_point = 1
    flag_point = 0
    for symbol_number_2 in user_number_2:
        if symbol_number_2.isdigit():
            result_number_2 += symbol_number_2
        elif symbol_number_2 == "." and flag_point == 0:
            result_number_2 += symbol_number_2
            flag_point = 1
    result_number_1 = float(result_number_1)
    result_number_2 = float(result_number_2)
    if user_operator in ("+", "-", "*", "/"):
        if user_operator == "+":
            result_calculation = result_number_1+result_number_2
        elif user_operator == "-":
            result_calculation = result_number_1-result_number_2
        elif user_operator == "*":
            result_calculation = result_number_1*result_number_2
        elif user_operator == "/":
            if result_number_2 != 0:
                result_calculation = result_number_1/result_number_2
            else:
                result_calculation = "cannot be divided by 0"
    else:
        result_calculation = "operator is not + or - or * or /"
    print(f"result calculation: {result_calculation}")
    continue_run = input("If you want to continue the calculations, please enter 'y' or 'yes' ").lower()
print("*** Good luck! ***")

# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується, по черзі, ввести числа та дію над цими числами,
# а програма, виходячи з дії, обчислює та друкує результат.

user_number_1 = int(input("Please enter a first number "))
user_number_2 = int(input("Please enter a second number "))
user_operator = input("Please enter a operator (+ or - or * or /) ")
result_calculation = 0
if user_operator == "+":
    result_calculation = user_number_1+user_number_2
elif user_operator == "-":
    result_calculation = user_number_1-user_number_2
elif user_operator == "*":
    result_calculation = user_number_1*user_number_2
elif user_operator == "/":
    if user_number_2 == 0:
        result_calculation = "cannot be divided by 0"
    else:
        result_calculation = user_number_1/user_number_2
else:
    result_calculation = "operator is not + or - or * or /"
print(f"result: {result_calculation}")

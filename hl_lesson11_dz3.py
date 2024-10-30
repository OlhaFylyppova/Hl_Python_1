# Ваша функція is_even, як і раніше, повинна повертати True якщо число парне, або False якщо число непарне, але при цьому
# НЕ МОЖНА використовувати ділення у функції, та дії пов'язані з ним. Тобто. заборонено використовувати /, //, % та divmod
# Складність ще полягає і в тому, щоб знайти рішення, яке не залежало б від розміру числа :)
# Вхідні дані: Ціле число. Вихідні дані: True або False


### варіант 1
print("* варіант 1 *")


def is_even(number):
    result_if = None
    my_number = str(number)
    if my_number[-1] in ("0", "2", "4", "6", "8"):
        result_if = True
    else:
        result_if = False
    print(f"number: {number}")
    print(f"result: {result_if}")
    return result_if


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'



### варіант 2
print("* варіант 2 *")


def is_even(number):
    my_number = str(number)
    print(f"number: {number}")
    print(f"result: {int(my_number[-1]) in range(0,9,2)}")
    return int(my_number[-1]) in range(0,9,2)


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

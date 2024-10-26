# Ваша функція is_even повинна повертати True якщо число парне, і False якщо число непарне.
# Вхідні дані: Ціле число. Вихідні дані: Логічний тип.


def is_even(digit):
    """ Перевірка чи є парним число """

    my_number = digit
    result_if = None
    if my_number % 2 == 0:
        result_if = True
    else:
        result_if = False
    print(f"number: {my_number}")
    print(f"result: {result_if}")
    return result_if


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

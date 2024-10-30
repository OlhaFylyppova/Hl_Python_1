# Напишіть функцію-генератор prime_generator, яка повертатиме прості числа. Верхня межа цього діапазону визначається
# параметром цієї функції. Наприклад, виклик функції list(prime_generator(10)) повинен відповідати послідовності з
# чисел [2, 3, 5, 7]. Наступне число в цій послідовності - 11 і воно більше 10 тому воно не потрапляє в цей ряд


def prime_generator(end):
    new_list = []
    result_list = []
    my_list = list(range(2, end + 1))
    for list_val in my_list:
        new_list = [list_val % val_t for val_t in range(2, end + 1)]
        if new_list.count(0) == 1:
            result_list.append(list_val)
            yield list_val
    print(f"prime numbers up to {end}: {result_list}")


from inspect import isgenerator

gen = prime_generator(1)

assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

# Є набір чисел (float або int). Вам потрібно знайти різницю між найбільшим (максимум) і найменшим (мінімум) елементом.
# Ваша функція difference має вміти працювати з невизначеною кількістю аргументів. Якщо аргументів немає, то функція
# повертає 0 (нуль). Якщо з 3-м тестом будуть проблеми, використовуйте функцію округлення round(x, 2), де х це число,
# яке потрібно округлити. Вх. Дані: Змінна кількість аргументів як числа (int, float).
# Вих. Дані: Різниця між максимумом і мінімумом як число (int, float).

def difference(*args):
    my_list = [*args]
    result_num = None
    print(f"start number list: {my_list}")
    if my_list:
        my_list.sort(reverse=True)
        result_num = my_list[0] - my_list[-1]
    else:
        result_num = 0
    if float(result_num):
        result_num = round(result_num, 2)
    print(f"result of difference: {result_num}")
    return result_num

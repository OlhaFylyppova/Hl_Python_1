# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range) для 100 елементів,
# за наступним правилом: Один список з числами кратними 3, інший з кратними числами 5. За допомогою множин створіть набір
# з числами, які є в обох множинах (перетин). Функція повинна повернути цю множину як результат своєї роботи.

def common_elements():
    my_list_3 = []
    my_list_5 = []
    for var_list in range(0, 100, 3):
        my_list_3.append(var_list)
    for var_list in range(0, 100, 5):
        my_list_5.append(var_list)
    my_set_3 = set(my_list_3)
    my_set_5 = set(my_list_5)
    result_set = my_set_3.intersection(my_set_5)
    print(f"result set: {result_set}")
    return result_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

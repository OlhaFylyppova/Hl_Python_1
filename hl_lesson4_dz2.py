# Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
# потім перемножити цю суму на останній елемент вхідного масиву. Не забудьте, що перший елемент
# масиву має індекс 0. Для порожнього масиву результат завжди 0.


### 1 варіант ###

print("*** 1 ***")
my_list = [1, 3, 5]
print(f"start list: {my_list}")
sum_list = 0
result_calculation = 0
list_len = len(my_list)
if list_len > 0:
    for num_list in range(0, list_len, 2):
        sum_list += my_list[num_list]
    result_calculation = sum_list*my_list[-1]
print(f"result: {result_calculation}")


### 2 варіант ###

print("*** 2 ***")
my_list = [1, 3, 5]
print(f"start list: {my_list}")
result_calculation = 0
list_len = len(my_list)
if list_len > 0:
    result_calculation = sum(my_list[::2])*my_list[-1]
print(f"result: {result_calculation}")

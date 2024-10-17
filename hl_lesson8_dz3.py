# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел, знаходить серед них унікальне число
# та повертати його. Унікальне число - це число, яке зустрічається в списку один раз. Випадок, коли в одному списку
# буде кілька унікальних чисел, перевіряти не потрібно.

def find_unique_value(some_list):
    my_list = some_list
    result_number = None
    my_set = set(my_list)
    for var_set in my_set:
        if my_list.count(var_set) == 1:
            result_number = var_set
            break
    print(f"list: {my_list}")
    print(f"unique number: {result_number}")
    return result_number

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

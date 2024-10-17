# Ваше завдання — написати функцію add_one, яка приймає список із цифр, які у свою чергу є одним числом. До нього необхідно
# додати 1. Тобто. Вам необхідно з набору цифр, що входять до списку, отримати число, скласти його з 1 і отриману суму,
# знову розбити на список із цифр. В результаті функція повертає список із цифр, що становлять значення суми.
# Так зі списку з цифрами [1, 2, 3, 4], має вийти число 1234. До нього додаємо 1, і отримуємо 1235. Після цього потрібно
# розбити отримане число на складові цифри. У результаті має бути список [1, 2, 3, 5], який повертає функція.


### варіант 1 ###

def add_one(some_list):
    my_list = some_list
    new_str = ''
    for str_var in my_list:
        new_str += str(str_var)
    str_list = str(int(new_str) + 1)
    new_list = list(str_list)
    for str_var in range(len(new_list)):
        new_list[str_var] = int(new_list[str_var])
    print(f"start list: {my_list} => result list: {new_list}")
    return new_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


### варіант 2 ###

def add_one(some_list):
    my_list = some_list
    new_str = 0
    len_list = len(my_list) - 1
    for str_var in my_list:
        new_str += str_var * (10 ** len_list)
        len_list -= 1
    new_list = list(str(new_str + 1))
    for str_var in range(len(new_list)):
        new_list[str_var] = int(new_list[str_var])
    print(f"start list: {my_list} => result list: {new_list}")
    return new_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

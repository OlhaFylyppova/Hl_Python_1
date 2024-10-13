# Написати функцію say_hi, яка представить людину за переданими параметрами.
# Вхідні дані: Два аргументи рядок(str) та позитивне число(int).
# Функція має повернути рядок.


### варіант 1 ###

def say_hi(name, age):
    my_string = "Hi. My name is {} and I'm {} years old"
    print(f"result 1: {my_string.format(name, age)}")
    return my_string.format(name, age)

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')


### варіант 2 ###

def say_hi(name, age):
    my_string = f"Hi. My name is {name} and I'm {age} years old"
    print(f"result 2: {my_string}")
    return my_string

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

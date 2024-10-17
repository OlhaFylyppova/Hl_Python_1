# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом. Паліндромом - це такий
# рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False

def is_palindrome(text):

    import string

    my_string = text
    print(f'string: "{my_string}"')
    my_string = my_string.lower().replace(" ", "")
    if any(char in string.punctuation for char in my_string):
        for symbol_str in string.punctuation:
            my_string = my_string.replace(symbol_str, "")
    reverse_string = my_string[::-1]
    print(f"result: {reverse_string == my_string}")
    return reverse_string == my_string

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

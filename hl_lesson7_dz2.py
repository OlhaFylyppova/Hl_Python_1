# На вхід функції correct_sentence передається два речення. Необхідно повернути їх виправлену копію так, щоб вони завжди
# починалися з великої літери та закінчувалися крапкою. Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже
# закінчується крапкою, додавати ще одну не потрібно, це буде помилкою.
# Вхідні аргументи: string. Вихідні аргументи: string.

def correct_sentence(text):
    my_sentence = text
    first_letter = my_sentence[0]
    if not first_letter.isupper():
        first_letter = first_letter.upper()
        my_sentence = first_letter + my_sentence[1:]
    if not my_sentence.endswith("."):
        my_sentence = my_sentence + "."
    print(f"result sentence: {my_sentence}")
    return my_sentence

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

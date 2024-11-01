# Ваше завдання написати функцію, яка прочитає заданий файл, очистить текст від html-тегів і запише цей текст в інший
# файл. html-тег завжди починається з "<" і закінчується на ">" тобто. потрібно видалити ці символи та все, що між ними.
# Функція отримує на вхід два параметри – ім'я файлу, який потрібно очистити, та ім'я файлу, куди потрібно записати
# очищений текст. Ім'я файлу, куди потрібно писати, можна задати за замовчуванням. Приклади файлів у вкладенні – файл
# який потрібно очистити (draft.html) та приклад файлу, який може вийти на виході з очищеним текстом (cleaned.txt).
# Файл draft.html необхідно скачати і покласти поряд з файлом, де буде вирішення цієї домашки.
# Додаткове завдання для тих, хто захоче ускладнити рішення - спробуйте прибрати рядки, в яких немає інформації.



### варіант 1
print("\n* варіант 1 *")

import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    n1 = html.find(">")
    n_end = html.rfind(">")
    n2 = html.find("<")
    n2 = html.find("<", n2 + 1)
    new_text = ""
    new_list = []
    result_list = []
    result_text = ""
    while n1 < n_end:
        new_text = new_text + html[n1+1:n2]
        n1 = html.find(">", n1+1)
        n2 = html.find("<", n2+1)
    new_text = new_text + html[n1+1:]
    new_list = new_text.splitlines()
    for value in new_list:
        if not value.isspace() and value != '':
            value = value.strip()
            result_list.append(value)
    result_text = "\n".join(result_list)
    with codecs.open(result_file, 'w', 'utf-8') as my_file:
        my_file.write(result_text)
    with codecs.open(result_file, 'r', 'utf-8') as my_file:
        print(my_file.read())


delete_html_tags('draft.html')



### варіант 2
print("\n* варіант 2 *")

import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    my_text = re.sub(r'(<(/?[^>]+)>)', '', html)
    new_list = my_text.splitlines()
    new_list = list(filter(lambda val_list: len(val_list) > 0 and not val_list.isspace(), new_list))
    new_list = [val_list.strip() + "\n" for val_list in new_list]
    with codecs.open(result_file, 'w', 'utf-8') as my_file:
        my_file.writelines(new_list)
    with codecs.open(result_file, 'r', 'utf-8') as my_file:
        print(my_file.read())


delete_html_tags('draft.html')



### варіант 3
print("* варіант 3 *")

import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    my_text = re.sub(r'(<(/?[^>]+)>)', '', html)
    new_list = my_text.splitlines()
    new_list = [value.strip() for value in new_list if not value.isspace() and value]
    result_text = "\n".join(new_list)
    with codecs.open(result_file, 'w', 'utf-8') as my_file:
        my_file.write(result_text)
    with codecs.open(result_file, 'r', 'utf-8') as my_file:
        print(my_file.read())


delete_html_tags('draft.html')

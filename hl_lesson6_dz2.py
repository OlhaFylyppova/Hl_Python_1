# Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді. Користувач повинен ввести число
# більше або дорівнює 0 і менше ніж 8640000. Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
# Ну і додатковим завданням є турбота про виведення. Слово "день" підбирається на основі кількості днів, а години, хвилини і секунди
# повинні заповнюватися нулями при одноцифрових значеннях. Підказка: одна хвилина - 60 сек. В одній годині 60 * 60 сек, в одній добі
# 24 * 60 * 60 сек. Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти відповідну кількість днів,
# годин, хвилин, а те що залишиться - це секунди, які менше 60 ;) Доповнити провідними нулями можна за допомогою методу zfill(2)

start_number = input("Будь ласка, зазначте кількість секунд (від 0 до 8639999 включно): ")

num_days = 0
num_hours = 0
num_minutes = 0
num_seconds = 0
result_time = ""
str_days = "днів"

if start_number.isdigit():
    start_number = int(start_number)
    if 0 <= start_number <= 8639999:
        num_days, num_var = divmod(start_number, 86400)
        num_hours, num_var = divmod(num_var, 3600)
        num_minutes, num_seconds = divmod(num_var, 60)
        if num_days in (2, 3, 4) or (num_days > 20 and num_days%10 in (2, 3, 4)):
            str_days = "дні"
        elif num_days == 1 or (num_days > 20 and num_days%10 == 1):
            str_days = "день"
        result_time = f'результат: "{start_number}" => {num_days} {str_days}, {str(num_hours).zfill(2)}:{str(num_minutes).zfill(2)}:{str(num_seconds).zfill(2)}'
    else:
        result_time = f'результат: внесене значення "{start_number}" - не коректне'
else:
    result_time = f'результат: внесене значення "{start_number}" - не є числовим'
print(result_time)
